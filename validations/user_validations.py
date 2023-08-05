from flask import request, jsonify, abort, make_response
from model.user import User


errors = []


def empty_fields(name, surname, username, password, email):
    if request.json['name'] == '' or request.json['surname'] == '' or \
            request.json['username'] == '' or \
            request.json['password'] == '' or \
            request.json['email'] == '':
        return False
    return True


def username_unique_validation(username):
    user_by_username = User.query.filter_by(username=username).first()

    if user_by_username is not None:
        return False
    return True


def email_unique_validation(email):
    user_by_email = User.query.filter_by(email=email).first()
    if user_by_email is not None:
        return False
    return True


def get_user_validation_errors(name, surname, username, password, email):
    errors.clear()
    user_valid = True
    if not username_unique_validation(username):
        user_valid = False
        errors.append({'code': '600', 'message': 'El nombre de usuario  ya existe'})

    if not email_unique_validation(email):
        user_valid = False
        errors.append({'code': '601', 'message': 'El email ya existe'})

    if not empty_fields(name, surname, username, password, email):
        user_valid = False
        errors.append({'code': '603', 'message': 'Los campos son obligatorios'})

    return make_response(errors, 400)
