from model.user import User, user_schema, users_schema
from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from services.user_service import save_user_service
from services.role_service import rol_by_id_service
from validations.user_validations import get_user_validation_errors, username_unique_validation, email_unique_validation, empty_fields

users_routes = Blueprint('users_routes', __name__, url_prefix="/api/user")


@users_routes.post("")
def save_user():
    name = request.json['name']
    surname = request.json['surname']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if not username_unique_validation(username) or not email_unique_validation(email) \
            or not empty_fields(name, surname, username, password, email):
        return get_user_validation_errors(name, surname, username, password, email)

    password_hash = generate_password_hash(password)

    roles = []
    role = rol_by_id_service(1)
    roles.append(role)

    user_by_request = User(name, surname, username, password_hash, email, roles)
    user_saved = save_user_service(user_by_request)

    return user_schema.dump(user_saved)








