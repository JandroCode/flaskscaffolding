from database.db import db
from model.user import User
from werkzeug.security import check_password_hash


def save_user_service(user):
    db.session.add(user)
    db.session.commit()
    return user


def find_roles_by_username(username):
    user = User.query.filter_by(username=username).first()
    roles = user.roles

    if user:
        return roles
    else:
        return ""
