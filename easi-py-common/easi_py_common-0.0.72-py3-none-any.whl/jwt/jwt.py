import uuid

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired

from easi_py_common.core.error import InvalidTokenException, TokenExpiredException
from easi_py_common.jwt.constants import JwtConstants


class Jwt:

    def __init__(self, secret_key: str = '', refresh_secret_key: str = ''):
        if not secret_key:
            secret_key = current_app.config['JWT_SECRET_KEY']
            refresh_secret_key = current_app.config['JWT_REFRESH_SECRET_KEY']
        self.secret_key = secret_key
        self.refresh_secret_key = refresh_secret_key

    def create_token(self, id: int, expires_in: int = JwtConstants.DEFAULT_EXPIRED_IN, city_id: int = None) -> str:
        s = self.__get_jw_serializer(self.secret_key, expires_in)
        return self.__create_token(s, id, city_id)

    def create_refresh_token(self, id: int, expires_in: int = JwtConstants.DEFAULT_REFRESH_EXPIRED_IN) -> str:
        s = self.__get_jw_serializer(self.refresh_secret_key, expires_in)
        return self.__create_token(s, id)

    def parse_token(self, token: str) -> int:
        s = self.__get_jw_serializer(self.secret_key)
        return self.__parse_token(s, token)

    def parse_refresh_token(self, refresh_token: str) -> int:
        s = self.__get_jw_serializer(self.refresh_secret_key)
        return self.__parse_token(s, refresh_token)

    def __create_token(self, s: Serializer, id: int, city_id=None):
        if city_id:
            return s.dumps({'id': id, 'uid': uuid.uuid1().__str__(), 'city_id': city_id}).decode('ascii')
        else:
            return s.dumps({'id': id, 'uid': uuid.uuid1().__str__()}).decode('ascii')

    def __parse_token(self, s: Serializer, token: str) -> int:
        try:
            data = s.loads(token)
        except SignatureExpired:
            raise TokenExpiredException()
        except Exception:
            raise InvalidTokenException()
        if 'id' not in data:
            raise InvalidTokenException()
        return int(data['id'])

    def __parse_city_id(self, s: Serializer, token: str) -> int:
        try:
            data = s.loads(token)
        except SignatureExpired:
            raise TokenExpiredException()
        except Exception:
            raise InvalidTokenException()
        if 'city_id' not in data:
            raise InvalidTokenException()
        return int(data['city_id'])

    @staticmethod
    def __parse_token_expire_timestamp(s: Serializer, token: str) -> int:
        try:
            header = s.loads(token, return_header=True)[1]
        except SignatureExpired:
            raise TokenExpiredException()
        except Exception:
            raise InvalidTokenException()

        return int(header['exp'])

    def token_expire_timestamp(self, token: str) -> int:
        s = self.__get_jw_serializer(self.secret_key)
        return self.__parse_token_expire_timestamp(s, token)

    def token_city_id(self, token: str) -> int:
        s = self.__get_jw_serializer(self.secret_key)
        return self.__parse_city_id(s, token)

    def __get_jw_serializer(self, secret_key: str, expires_in: int = 3600) -> Serializer:
        return Serializer(secret_key,
                          expires_in=expires_in,
                          algorithm_name=JwtConstants.SERIALIZER_ALGORITHM_NAME)


# if __name__ == '__main__':
#     from easi_py_common.core.flasky import AppWrapper
#     app_wrapper = AppWrapper('api')
#     app = app_wrapper.get_app()
#     app.app_context().push()
#
#     token = Jwt().create_token(1)
#     print(token)
#     city_id = Jwt().token_city_id(token)
#     print(city_id)
