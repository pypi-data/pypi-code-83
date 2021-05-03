# It can handle both session and token authorization
# Created on Feb 12, 2020 by Hans Roh (hansroh@gmail.com)

try:
    from firebase_admin import auth
except ImportError:
    pass
from collections import namedtuple
import time
import datetime
import os
from . import services
from .services import UserService

AUTH_SESSION_NAME = 'STK'
TEMPLATE_DIR = 'pages/examples'

class CurrentUser:
    def __init__ (self, uid, lev, nick_name):
        self.uid = uid
        self.lev = lev
        self.nick_name = nick_name
        self.tuid = None

    def __str__ (self):
        return self.uid

def user_exists (was, user):
    if user.status:
        if user.status == 'unverified':
            return True
        if user.status == 'resigned':
            if user.last_updated < datetime.datetime.today ().astimezone (datetime.timezone.utc) - datetime.timedelta(days=7):
                UserService.set (user.uid, {'uid': None}).commit ()
                return False
            else:
                return True
        raise was.Error ("403 Forbidden", {'status': user.status, 'uid': user.uid, 'nick_name': user.nick_name})
    return True

# Session ---------------------------------------
ALLOWED_STATUS = {'resigned', 'unverified'}
def check_session (was):
    was.session.mount (AUTH_SESSION_NAME, was.app.config.TIMEOUT_LTS, extend = False)
    uid = was.session.get ('uid')
    if not uid:
        if not was.request.acceptable ('text/html'):
            raise was.Error ("401 Unauthorized")
        return was.response ("401 Authorization Required", was.render (os.path.join (TEMPLATE_DIR, 'auth/signin-form.j2').replace ('\\', '/')))
    if was.session.use_time () > was.app.config.TIMEOUT_STS:
        user = UserService.get (uid).one ()
        if user.status and user.status not in ALLOWED_STATUS:
            was.session.expire ()
            raise was.Error ("403 Forbidden", "status {}".format (user.status))
        was.session.set ('nick_name', user.nick_name) # refresh recent nick_name
        was.session.touch ()
    was.request.user = CurrentUser (uid, was.session ['lev'], was.session ['nick_name'])


def __mount__ (app, options):
    global TEMPLATE_DIR

    if 'AUTH_TEMPLATE_DIR' in app.config:
        path = app.config ['AUTH_TEMPLATE_DIR']
        if path and path [-1] != '/':
            path = path + '/'
        TEMPLATE_DIR = path


    # JWT -----------------------------------------
    def check_jwt (was):
        claims = was.dejwt ()
        if "err" in claims:
            raise was.Error ("401 Unauthorized", claims ["err"])
        was.request.user = CurrentUser (claims ['uid'], claims ['lev'], claims ['nick_name'])

    def validate_refresh_token (was, token):
        claims = was.dejwt (token)
        if 'err' in claims:
            raise was.Error ("401 Unauthorized", claims ["err"], 40100)
        if not claims.get ("is_refresh"):
            raise was.Errort ("400 Bad Request", "invalid refresh token", 40001)
        user = UserService.get (uid = claims ['uid']).one ()
        if not user_exists (was, user):
            raise was.Error ("404 User Not Found")
        return user, claims

    def to_payload (account):
        return {
            "nick_name": account.nick_name,
            "uid": account.uid,
            "lev": account.lev
        }

    def make_token (was, user, is_refresh = False):
        exp = time.time () + was.app.config.get (is_refresh and "TIMEOUT_LTS" or "TIMEOUT_STS")
        payload = {
            "iat": time.time (),
            "exp": exp,
            "iss": was.request.get_header ('host', '').split (":", 1) [0],
            "lev": user ["lev"],
            "uid": user ["uid"],
            'nick_name': user ['nick_name']
        }
        if is_refresh:
            payload ["is_refresh"] = True
        return was.mkjwt (payload), exp

    def make_both_tokens (was, user):
        access_token, _ = make_token (was, user)
        refresh_token, _ = make_token (was, user, True)
        return {
            "lev": user ["lev"],
            "uid": user ["uid"],
            "nick_name": user ["nick_name"],
            "access_token": access_token,
            "refresh_token": refresh_token
        }


    # handlers -----------------------------------------------------
    @app.permission_check_handler
    def permission_check_handler (was, perms):
        if was.request.get_header ('authorization'):
            output = check_jwt (was)
        else:
            output = check_session (was)
        if output:
            return output

        if 'uid' in was.request.PARAMS:
            tuid = was.request.PARAMS ['uid']
            if 'owner' in perms and tuid != 'me':
                raise was.Error ("403 Permission Denied", "owners only operation")
            was.request.user.tuid = (tuid == 'me' and was.request.user.uid or (tuid != 'notme' and tuid or None))

        if not perms:
            return

        if was.request.user.lev == "staff" or "user" in perms:
            return # always vaild
        if "staff" in perms:
            raise was.Error ("403 Permission Denied")

    @app.route ("/signin", methods = ["GET"])
    def signin (was, provider = None, return_url = '', state = '', **payload):
        if state.startswith ('kakao:'):
            was.request.ARGS ['provider'], _, return_url = state.split (":", 2)

        # preventing infinite loop
        if return_url.startswith (was.baseurl (signin)):
            query = return_url.split ("?", 1)
            if len (query) == 1:
                return_url = None
            else:
                for p in query [1].split ('&'):
                    if p.startswith ('return_url='):
                        return_url = p [11:]

        was.request.ARGS ['return_url'] = return_url
        return was.render (
            os.path.join (TEMPLATE_DIR, 'auth/signin-form.j2').replace ('\\', '/'),
            provider = provider,
            next_url = return_url or options.get ('return_url', '/')
        )

    @app.route ("/signup", methods = ["GET", "OPTIONS"])
    def signup (was, return_url = None):
        return was.render (os.path.join (TEMPLATE_DIR, 'auth/signup-form.j2').replace ('\\', '/'), next_url = return_url or options.get ('return_url', '/'))

    @app.route ("/password", methods = ["GET", "OPTIONS"])
    @app.permission_required ()
    def password (was):
        return was.render (os.path.join (TEMPLATE_DIR, 'auth/password-form.j2').replace ('\\', '/'))

    @app.route ("/signout", methods = ["GET"])
    @app.permission_required ()
    def signout (was, return_url = None):
        app.emit ('signout', was.request.user.uid)
        was.remove_csrf ()
        was.session.mount (AUTH_SESSION_NAME, was.app.config.TIMEOUT_LTS)
        was.session.expire ()
        return was.render (os.path.join (TEMPLATE_DIR, 'auth/signout.j2').replace ('\\', '/'), next_url = return_url or options.get ('return_url', '/'))

    # firebase -----------------------------------------------------
    @app.route ('/firebase_custom_token', methods = ["POST", "OPTIONS"])
    def firebase_custom_token (was, provider, access_token, payload = None):
        if 'firebaseConfig' not in was.app.config.FRONTEND:
            raise was.Error ('510 Not Extended', 'firebase is not configured')

        if payload is None:
            endpoint = services.PROVIDERS.get (provider)
            if not endpoint:
                raise was.Error ("400 Unknown OAuth Provider")
            resp = was.get (endpoint, headers = {'Authorization': 'Bearer {}'.format (access_token)})
            payload = resp.fetch ()

        uid, profile = services.get_uid_and_profile (provider, payload)
        return was.API (
            custom_token = auth.create_custom_token (uid).decode (),
            profile = profile,
            urls = { 'signin': was.urlspec (signin_with_firebase_id_token) }
        )

    # signin methods --------------------------------------------------
    @app.route ("/firebase/users/<uid>", methods = ["GET"])
    def firebase_users (was, uid):
        user = UserService.get (uid).fetch ()
        if user and not user_exists (was, user [0]):
            user = []
        if not user:
            raise was.Error ('404 Not Found')
        return was.API ()

    @app.route ("/signin_with_firebase_id_token", methods = ["POST", "OPTIONS"])
    @app.inspect (lists = ['returns'])
    def signin_with_firebase_id_token (was, id_token, profile = None, returns = None, decoded_token = None):
        profile = profile or {}
        if 'lev' in profile:
            raise was.Error ('400 Bad Request', 'cannot set permission')
        if decoded_token is None:
            decoded_token = auth.verify_id_token (id_token)
        else:
            assert decoded_token ['uid'].startswith ('UNITTEST')

        uid = decoded_token ['uid']
        user = UserService.get (uid).fetch ()
        if user and not user_exists (was, user [0]):
           user = []

        email_verified = True
        if decoded_token.get ('firebase', {}).get ('sign_in_provider') == 'password':
            # only pasword provider can be sure email_verified
            email_verified = decoded_token ['email_verified']

        if not user:
            is_member = False
            if profile.get ('nick_name'):
                if UserService.get (nick_name = profile ['nick_name']).fetch ():
                    raise was.Error ('409 Conflict', 'nick name is already in used', 40920)
            if email_verified is False:
                profile ['status'] = 'unverified'
                profile ['email_verified'] = False
            else:
                profile ['email_verified'] = True
            if profile:
                user = UserService.add (uid, profile).one ()

        else:
            is_member = True
            user = user [0]
            if not user.email_verified and email_verified:
                profile ['status'] = None
                profile ['email_verified'] = True
            if profile:
                user = UserService.set (uid, profile).one ()

        if 'lev' in decoded_token:
            UserService.set (uid, {'lev': decoded_token ['lev']}).commit ()
            user.lev = decoded_token ['lev']

        was.session.mount (AUTH_SESSION_NAME, was.app.config.TIMEOUT_LTS)
        was.session.set ('uid', decoded_token ['uid'])
        was.session.set ('lev', user.lev)
        was.session.set ('nick_name', user.nick_name)
        if user.status:
            was.session.set ('status', user.status)
        was.generate_csrf () # create initial token
        app.emit ('signin', user.uid, is_member)
        payload = make_both_tokens (was, to_payload (user))
        return was.API (
            is_member and "200 OK" or "201 Created",
            is_member = is_member,
            status = user.status,
            email_verified = user.email_verified,
            last_updated = user.last_updated,
            links = {
                'profile': was.urlspec ('helpers.firebase.users.get_profile'),
                'signout': was.urlspec (signout),
                'extend_access_token': was.urlspec (extend_access_token),
                'extend_refresh_token': was.urlspec (extend_refresh_token),
            },
            **payload
        )

    @app.route ("/nick_names/<nick_name>", methods = ["PUT", "GET", "OPTIONS"])
    @app.clarify_permission
    @app.inspect (nick_name__len__between = (2, 40))
    def nick_name (was, nick_name):
        if was.request.user:
            if was.request.user.nick_name == nick_name:
                return was.API ('202 Creatable')

        users = UserService.get (nick_name = nick_name).fetch ()
        if users:
            raise was.Error ('409 Conflict', 'nickname is already in used')
        else:
            return was.API ('201 Creatable')

    # extending tokens -----------------------------------------------
    @app.route ("/refresh_token", methods = ["POST", "OPTIONS"])
    @app.inspect (booleans = ['force'])
    @app.permission_required ()
    def extend_refresh_token (was, refresh_token, force = False):
        user, claims = validate_refresh_token (was, refresh_token)
        if force and not claims ['uid'].startswith ('UNITTEST'):
            raise was.Error ("403 Permission Denied", "you have not permission for forcing", 40310)
        if not force and claims ["exp"] - time.time () > was.app.config.TIMEOUT_LTS * 0.25:
            raise was.Error ("409 Conflict", "refresh token is still valid", 41210)
        payload = make_both_tokens (was, to_payload (user))
        return was.API (payload)

    @app.route ("/access_token", methods = ["POST", "OPTIONS"])
    def extend_access_token (was, refresh_token):
        user, claims = validate_refresh_token (was, refresh_token)
        access_token, _ = make_token (was, to_payload (user))
        return was.API (nick_name = user.nick_name, access_token = access_token)

    @app.route ("/csrf_token", methods = ["GET"])
    def csrf_token (was):
        return was.API ("200 OK", token = was.csrf_token, name = was.CSRF_NAME)
