from database.db import db
from flask_marshmallow import Marshmallow

# Tabla de unión (Asociación entre Usuarios y Proyectos)
users_roles = db.Table('users_roles',
                       db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                       db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
                       )


# Modelo para la tabla Usuario
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(200))

    roles = db.relationship('Role', secondary=users_roles, backref='users', lazy='dynamic')

    def __init__(self, name, surname, username, password, email, roles):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.email = email
        self.roles = roles


ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
