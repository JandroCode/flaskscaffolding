from flask import request, jsonify, abort, Blueprint, make_response
from security.security import Security

user_auth_routes = Blueprint('user_auth_routes', __name__, url_prefix="/api/auth")


@user_auth_routes.post("")
def demo_user():
    valid_token = Security.verify_token(request.headers)

    if not valid_token:
        response = jsonify({'status': 'error'})
        return make_response(response, '401')

    payload = Security.decode_jwt(request.headers)
    role = payload['roles']

    if role == 'USER':
        return jsonify({'message': 'Hola User'})
    else:
        response = jsonify({'error': '401'})
        return make_response(response, 401)
