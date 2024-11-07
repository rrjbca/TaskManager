from flask import Blueprint

from .tasks import blueprint as tasks_blueprint
from .users import blueprint as users_blueprint

blueprint = Blueprint('views', __name__)

blueprint.register_blueprint(tasks_blueprint)
blueprint.register_blueprint(users_blueprint)
