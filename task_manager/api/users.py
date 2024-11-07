from flask import Blueprint, jsonify, request

from database import database
from models import User

blueprint = Blueprint('users', __name__)


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    user = User(**request.json)
    database.session.add(user)
    database.session.commit()
    return jsonify(user.as_dict())


@blueprint.route('/api/users', methods=['GET'])
def get_users():
    user_list = [user.as_dict() for user in User.query.all()]
    return jsonify(user_list)
