import requests
from flask import Blueprint, render_template, url_for

blueprint = Blueprint('tasks', __name__)


@blueprint.route('/tasks')
def index():
    get_tasks_url = url_for('api.tasks.get_tasks', _external=True)
    response = requests.get(get_tasks_url)
    return render_template('task_list.html', tasks=response.json())
