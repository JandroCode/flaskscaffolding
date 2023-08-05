from model.role import Role, role_schema, roles_schema
from flask import Blueprint, request, jsonify

roles_routes = Blueprint('roles_routes', __name__, url_prefix="/api/role")


@roles_routes.post("")
def find_role(id):
    role = Role.query.filter_by(id=id).first()
    return role_schema.dump(role)
