import jwt
import requests
from datetime import datetime

class Signer:
    def __init__(self, private_key):
        self.private_key = private_key

    def sign(self, user_id, site_id, name="", email="", avatar=""):
        encoded_jwt = jwt.encode({
            "iss": site_id,
            "sub": user_id,
            "iat": datetime.utcnow(),
            "name": name,
            "email": email,
            "avatar": avatar,
            }, self.private_key, algorithm="HS512")
        return encoded_jwt

    def getUserSubscription(self, user_id):
        r = requests.get(f"https://sponsor-api.nitropay.com/v1/users/{user_id}/subscription", headers={'Authorization': self.private_key})
        if r.status_code != 200:
            return {}
        return r.json()

