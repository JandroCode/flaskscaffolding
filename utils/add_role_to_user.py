from services.role_service import rol_by_id_service


def add_role():
    roles = []
    role = rol_by_id_service(2)
    roles.append(role)
    return roles
