from flask import Blueprint, jsonify, request

from database import database
from models import Task

blueprint = Blueprint('tasks', __name__)


@blueprint.route('/api/tasks', methods=['POST'])
def create_task():
    task = Task(**request.json)
    database.session.add(task)
    database.session.commit()
    return jsonify(task.as_dict())


@blueprint.route('/api/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.as_dict() for task in Task.query.all()]
    return jsonify(task_list)


@blueprint.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    for k, v in request.json.items():
        setattr(task, k, v)
    database.session.commit()
    return jsonify(task.as_dict())
