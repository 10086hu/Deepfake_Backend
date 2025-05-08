from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.orm import defer
import os
from app.encrypt import check_password, set_password
from app.init import db
from app.model.detection import Detection
from app.model.user import User
from app.result import Result
from tool import detection_to_dict

bp = Blueprint('main', __name__)


@bp.route('/user/login', methods=['POST'])
def user_login():
    username = request.form.get("username", None)
    password = request.form.get("password", None)

    user = User.query.filter_by(username=username).first()
    if user is None:
        return Result.fail({"content": "用户不存在"})
    if check_password(password, user.password):
        return Result.ok({"token": create_access_token(identity=str(user.id))})
    else:
        return Result.fail({"content": "密码错误"})


@bp.route('/user/register', methods=['POST'])
def user_register():
    username = request.form.get("username", None)
    password = request.form.get("password", None)
    confirm_password = request.form.get("confirm_password", None)
    email = request.form.get("email", None)

    if password != confirm_password:
        return Result.fail({"content": "密码与确认密码不一致"})

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return Result.fail({"content": "用户名已存在"})
    user = User.query.filter_by(email=email).first()
    if user is not None:
        return Result.fail({"content": "该邮箱已被注册"})

    encrypted_password = set_password(password)
    try:
        new_user = User(
            username=username,
            avatar_url="是图片url",
            password=encrypted_password,
            email=email
        )
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Result.fail({"content": e})

    current_user = User.query.filter_by(username=username).first()
    return Result.ok({"token": create_access_token(identity=current_user.id)})


@bp.route('/user/record', methods=['GET'])
@jwt_required()
def user_record():
    id = int(get_jwt_identity())
    detections = Detection.query.filter_by(user_id=id).options(defer(Detection.id), defer(Detection.user_id)).order_by(
        Detection.time.desc()).all()

    detections_dict = [detection_to_dict(d) for d in detections]

    return Result.ok({"detections": detections_dict})


@bp.route('/user/info', methods=['GET'])
@jwt_required()
def user_info():
    id = int(get_jwt_identity())
    info = User.query.filter_by(id=id).options(defer(User.id), defer(User.password)).first()

    if info is None:
        return Result.fail({"content": "未查询到用户信息，请重新登录"})

    return Result.ok({"username": info.username, "avatar_url": info.avatar_url, "email": info.email})


news_bp = Blueprint('news', __name__)


@bp.route('/news/detect', methods=['POST'])
@jwt_required(optional=False)
def news_detect() -> (jsonify, int):
    userid = int(get_jwt_identity())
    file = request.files['image']
    app_dir = os.path.dirname(os.path.abspath(__file__))
    resource_dir = os.path.join(app_dir, 'static/news')

    os.makedirs(resource_dir, exist_ok=True)
    save_path = os.path.join(resource_dir, file.filename)
    #以后可以使用日期做分桶操作、例如dirname + datetime 加快查询速度
    file.save(save_path)
    result = 0
    text = request.form.get('text')
    if text[0].isdigit():
        result = 1
    try:
        new_detection = Detection(content=text, picture_url=save_path, result=result, user_id=userid)
        db.session.add(new_detection)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Result.fail({'content': e})
    return Result.ok({'data': result})
