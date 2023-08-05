from database.db import db
from flask_marshmallow import Marshmallow


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)

    def __init__(self, name):
        self.name = name


ma = Marshmallow()


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

