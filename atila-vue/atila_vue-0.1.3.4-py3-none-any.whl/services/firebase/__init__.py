from . import users, auth
from .services import UserService

def __setup__ (app, options):
    app.mount ('/auth', auth, return_url = options.get ('return_url', '/'))
    app.mount ('/users', users)

    @app.on ('signin')
    def on_signin (was, uid, is_member):
        UserService.log (uid, {'action': is_member and 'signin' or 'signup'})

    @app.on ('signout')
    def on_signout (was, uid):
        UserService.log (uid, {'action': 'signout'})

    @app.on ('profile-changed')
    def on_profile_update (was, uid, payload):
        UserService.log (uid, {'action': 'update', 'payload': payload})

    @app.on ('resign')
    def on_resign (was, uid, cancel = False):
        UserService.log (uid, {'action': cancel and 'retract' or 'resign'})

    @app.on ('status-changed')
    def on_status_changed (was, uid, status):
        UserService.log (uid, {'action': status or 'activated'})
