from flask import Flask
from environments.dev.load_dev_env import config, get_database_config, get_secret_key
from database.db import init_app
from flask_cors import CORS
from controllers.user_controller import users_routes
from controllers.role_controller import roles_routes
from controllers.login_controller import login_routes
from controllers.admin_controller import admin_routes
from controllers.user_auth import user_auth_routes

app = Flask(__name__)

# CORS_CONFIG
app.config['JSON_AS_ASCII'] =False
CORS(app)

# DATABASE_CONFIG
host = get_database_config().get('MYSQL_HOST')
user = get_database_config().get('MYSQL_USER')
password = get_database_config().get('MYSQL_PASSWORD')
database = get_database_config().get('DATABASE_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user + '@' + host + '/' + database

# BLUEPRINTS
app.register_blueprint(users_routes)
app.register_blueprint(roles_routes)
app.register_blueprint(login_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(user_auth_routes)


init_app(app)

if __name__ == '__main__':
    app.config.from_object(config['dev'])
    app.run()
