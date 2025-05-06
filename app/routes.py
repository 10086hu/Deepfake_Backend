from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.encrypt import check_password
from app.model.user import User
from app.result import Result

bp = Blueprint('main', __name__)


@bp.route('/user/login', methods=['POST'])
def user_login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if user is None:
        return Result.fail({"content": "用户不存在"})
    if check_password(password, user.password):
        return Result.ok({"token": create_access_token(identity=user.id)})
    else:
        return Result.fail({"content": "密码错误"})


@bp.route('/user/register', methods=['POST'])
def user_register():
    return '222'


@bp.route('/user/record', methods=['GET'])
def user_record():
    return '333'


@bp.route('/news/detect', methods=['POST'])
def news_detect():
    return '444'
