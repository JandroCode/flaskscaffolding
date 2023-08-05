import datetime
import jwt
import pytz
from environments.dev.load_dev_env import get_secret_key
from services.user_service import find_roles_by_username


class Security():
    tz = pytz.timezone('Europe/Madrid')
    secret_key = get_secret_key()

    @classmethod
    def generate_token(cls, username):
        roles = find_roles_by_username(username)
        role_name = ""

        for rol in roles:
            role_name = rol.name

        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(hours=1),
            'username': username,
            'roles': role_name
        }
        return jwt.encode(payload, cls.secret_key, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            try:
                payload = jwt.decode(encoded_token, cls.secret_key, algorithms=['HS256'])
                return True
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False

        return False

    @classmethod
    def decode_jwt(cls, headers):
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            try:
                payload = jwt.decode(encoded_token, cls.secret_key, algorithms=['HS256'])
                return payload
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return False

        return False

