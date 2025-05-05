from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)


@bp.route('/user/login', methods=['POST'])
def user_login():
    return '111'


@bp.route('/user/register', methods=['POST'])
def user_register():
    return '222'


@bp.route('/user/record', methods=['GET'])
def user_record():
    return '333'


@bp.route('/news/detect', methods=['POST'])
def news_detect():
    return '444'
