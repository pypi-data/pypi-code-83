from .auth import AUTH_SESSION_NAME
import random
from .services import UserService

def __mount__ (app, options):
    @app.route ('/<uid>/profile', methods = ['GET'])
    @app.permission_required (uid = ['staff'])
    def get_profile (was, uid):
        return was.Map (
            profile__one = UserService.get (was.request.user.tuid),
            __mtime = 'profile.last_updated'
        )

    @app.route ('/<uid>/profile', methods = ['DELETE', 'OPTIONS'])
    @app.inspect (booleans = ['real', 'cancel'])
    @app.permission_required (uid = ['staff'])
    def delete_profile (was, uid, cancel = False, real = False):
        if real:
            mutation = UserService.delete (was.request.user.tuid)
        else:
            mutation = UserService.set (was.request.user.tuid, {'status': not cancel and 'resigned' or None})
            if cancel:
                was.session.remove ('status')
            else:
                was.session.set ('status', 'resigned')
            uid == 'me' and app.emit ('resign', was.request.user.uid, cancel)
        return was.Map ("201 No Content", mutation)

    UNMODIFIABLES = {'id', 'uid', 'lev', 'status'}
    @app.route ('/<uid>/profile', methods = ['PATCH', 'OPTIONS'])
    @app.permission_required (['owner'])
    def patch_profile (was, uid, **payload):
        if not was.request.user.nick_name and 'maybe_nick_name' in payload:
            maybe_nick_name = payload.pop ('maybe_nick_name')
            if maybe_nick_name:
                users = UserService.get (nick_name = maybe_nick_name).fetch ()
                if not users:
                    payload ['nick_name'] = maybe_nick_name
                else:
                    dups = { each.nick_name for each in users }
                    for i in range (10):
                        temp = '{}#{}'.format (maybe_nick_name, random.randrange (9999))
                        if temp not in dups:
                            payload ['nick_name'] = temp
                            break

        if payload.get ('nick_name'):
            if len (payload ['nick_name'].encode ()) > 24:
                raise was.Error ("400 Bad Request", 'too long nickname')

            if payload ['nick_name'] and payload ['nick_name'] != was.request.user.nick_name:
                user = UserService.get (nick_name = payload ['nick_name']).fetch ()
                if user:
                    payload ['nick_name'] = None
                elif uid == 'me':
                    was.session.mount (AUTH_SESSION_NAME, was.app.config.TIMEOUT_LTS, extend = False)
                    if was.session.get ('nick_name') != payload ['nick_name']:
                        was.session.set ('nick_name', payload ['nick_name'])
            else:
                payload.pop ('nick_name')

        for each in UNMODIFIABLES:
            if each in payload:
                raise was.Error ('403 Permission Denied', 'you have not permission for this operation')

        payload = { k: v for k, v in payload.items () if v not in ('', None) }
        if payload:
            uid == 'me' and app.emit ('profile-changed', was.request.user.uid, payload)
            return was.Map (UserService.set (was.request.user.tuid, payload), new_nick_name = was.session.get ('nick_name'))
        return was.API (new_nick_name = was.session.get ('nick_name'))

    @app.route ("/<uid>/permission", methods = ["PATCH", "OPTIONS"])
    @app.inspect (lev__in = ('staff', 'user'))
    @app.permission_required (['staff'])
    def set_permission (was, uid, status, lev = None):
        assert status != 'resigned', 'unacceptable status'
        app.emit ("status-changed", was.request.user.tuid, status)
        payload = {'status': status}
        if lev: payload ['lev'] = lev
        mutation = UserService.set (was.request.user.tuid, payload)
        return was.Map ("200 OK", mutation)
