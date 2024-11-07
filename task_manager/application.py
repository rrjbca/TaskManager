import tomllib

from flask import Flask

from database import database
from api import blueprint as api_blueprint

application = Flask(__name__)
application.config.from_file("config.toml", load=tomllib.load, text=False)

database.init_app(application)
with application.app_context():
    database.create_all()

application.register_blueprint(api_blueprint)

if __name__ == '__main__':
    application.run(debug=True)
