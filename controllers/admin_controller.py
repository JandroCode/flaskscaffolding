from flask import request, jsonify, abort, Blueprint, make_response
from security.security import Security

admin_routes = Blueprint('admin_routes', __name__, url_prefix="/api/admin")


@admin_routes.post("")
def demo_admin():
    valid_token = Security.verify_token(request.headers)

    if not valid_token:
        response = jsonify({'status': 'error'})
        return make_response(response, '401')

    payload = Security.decode_jwt(request.headers)
    role = payload['roles']

    if role == 'ADMIN':
        return jsonify({'message': 'Hola Admin'})
    else:
        response = jsonify({'error': '401'})
        return make_response(response, 401)