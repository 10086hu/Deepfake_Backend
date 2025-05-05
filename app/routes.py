from flask import Blueprint, request, jsonify

from app.model.user import User

bp = Blueprint('main', __name__)


@bp.route('/user/login', methods=['POST'])
def user_login():
    # 查询所有用户
    users = User.query.all()

    # 将用户数据转换为字典格式
    user_list = [{
        'id': user.id,
        'username': user.username,
        'avatar_url': user.avatar_url,
        'email': user.email
    } for user in users]

    return {'users': user_list}


@bp.route('/user/register', methods=['POST'])
def user_register():
    return '222'


@bp.route('/user/record', methods=['GET'])
def user_record():
    return '333'


@bp.route('/news/detect', methods=['POST'])
def news_detect():
    return '444'
