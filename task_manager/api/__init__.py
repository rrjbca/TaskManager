from flask import Blueprint

from .tasks import blueprint as tasks_blueprint

blueprint = Blueprint('api', __name__)

blueprint.register_blueprint(tasks_blueprint)
