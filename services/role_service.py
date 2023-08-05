from model.role import Role
from database.db import db


def rol_by_id_service(id):
    role = Role.query.filter_by(id=id).first()
    return role


