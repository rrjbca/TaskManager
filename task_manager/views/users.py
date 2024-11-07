from flask import Blueprint, render_template, url_for
import requests

blueprint = Blueprint('users', __name__)


@blueprint.route('/users')
def index():
    get_users_url = url_for('api.users.get_users', _external=True)
    response = requests.get(get_users_url)
    return render_template('user_list.html', users=response.json())


@blueprint.route('/new_user')
def new_user():
    return render_template('new_user.html')
