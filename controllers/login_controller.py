from flask import request, jsonify, abort, Blueprint, make_response
from security.security import Security
from werkzeug.security import check_password_hash
from model.user import User

login_routes = Blueprint('login_routes', __name__, url_prefix="/api/login")


@login_routes.post("")
def get_login():
    username = request.json['username']
    password = request.json['password']

    if username == '' or password == '':
        response = jsonify({'status': 'error'})
        return make_response(response, 400)

    user = User.query.filter_by(username=username).first()

    if user is not None:
        check_password_hash(username, password)
        token = Security.generate_token(username)
        return jsonify({'token': token})
    else:
        response = jsonify({'status': 'unauthorized'})
        return make_response(response, 401)

