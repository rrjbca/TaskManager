import tomllib

from flask import Flask

application = Flask(__name__)
application.config.from_file("config.toml", load=tomllib.load, text=False)

if __name__ == '__main__':
    application.run(debug=True)
