from flask import Blueprint

from .tasks import blueprint as tasks_blueprint

blueprint = Blueprint('views', __name__)

blueprint.register_blueprint(tasks_blueprint)
