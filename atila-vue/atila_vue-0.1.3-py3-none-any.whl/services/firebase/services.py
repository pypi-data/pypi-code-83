
from datetime import datetime
from skitai import was
import hashlib
import base64
from firebase_vue.models import User, UserLog

PROVIDERS = {
    'naver': 'https://openapi.naver.com/v1/nid/me',
    'kakao': 'https://kapi.kakao.com/v2/user/me'
}

def get_uid_and_profile (provider, payload):
    def gender_code (v):
        if not v:
            return ''
        if v.lower () in ('m', 'male'):
            return 'male'
        elif v.lower () in ('f', 'female'):
            return 'female'
        return 'etc'

    profile = {}
    profile ['providerId'] = provider
    if provider == 'kakao':
        id = payload ['id']
        account = payload ['kakao_account']
        profile ['displayName'] = account ['profile'].get ('nickname', '')
        profile ['photoURL'] = account ['profile'].get ('thumbnail_image_url', '')

    elif provider == 'naver':
        account = payload ['response']
        id = account ['id']
        profile ['displayName'] = account.get ('nickname', '')
        profile ['photoURL'] = account.get ('profile_image', '')

    profile ['uid'] = id
    profile ['birthday'] = account.get ('birthday', '').replace ('-', '')
    profile ['email'] = account.get ('email', '')
    profile ['gender'] = gender_code (account.get ('gender', ''))
    profile ['name'] = account.get ('name', '')
    profile ['phoneNumber'] = ''
    profile ['emailVerified'] = True # assume all true

    # make 28 bytes UID
    uid = '{}-{}'.format (provider, id)
    uid = base64.encodestring (hashlib.md5 (uid.encode ()).digest () + b'-cust') [:-1].decode ().replace ('/', '-').replace ('+', '.')
    return uid, profile


class UserService:
    @classmethod
    def _get_id (cls, uid):
        return User.get (uid = uid).get ('id')

    # basic ops ------------------------------
    @classmethod
    def get (cls, uid = None, nick_name = None):
        assert uid or nick_name, 'uid or nick_name required'
        return User.get (uid = uid, nick_name = nick_name).execute ()

    @classmethod
    def add (cls, uid, payload):
        payload ['uid'] = uid
        return User.add (payload).returning ("*").execute ()

    @classmethod
    def set (cls, uid, payload):
        return User.set (payload, uid = uid).returning ("*").execute ()

    @classmethod
    def delete (cls, uid):
        return (User.remove (uid = uid)
                        .with_ (UserLog.remove (user_id = cls._get_id (uid)))).execute ()

    # log -----------------------------------
    @classmethod
    def log (cls, uid, payload):
        payload ['user_id'] = cls._get_id (uid)
        return UserLog.add (payload).execute ()

    @classmethod
    def test (cls, payload):
        User.validate (payload)
