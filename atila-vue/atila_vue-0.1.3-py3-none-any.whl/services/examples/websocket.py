import skitai
from ..helpers import wsbgtask
import psutil

def onopen (was):
    wsbgtask.attach (was.request.ARGS ["userid"], was.websocket)

def onclose (was):
    wsbgtask.dettach (was.request.ARGS ["userid"])


def __mount__ (app, mntopt):
    @app.route ("")
    @app.websocket (skitai.WS_CHANNEL | skitai.WS_THREADSAFE, 300, onopen, onclose)
    def websocket (was, message, userid):
        if message.startswith ("run-mkclip "):
            if jobs.has_task (userid):
                return "error|You already have job"
            params = message.split (" ")[1]
            id, clips = params.split ("|")
            task = wsbgtask.Task (userid, was.websocket, was.app.config.MKCLIP, id, clips)
            task.start ()
            wsbgtask.add_job (userid, task)

        elif message ==  "cpu":
            return ">> cpu {:.1f}".format (psutil.cpu_percent ())

        elif message ==  "kill process":
            wsbgtask.kill (userid)
            return 'killed'

        return '{} said: {}'.format (userid, message)
