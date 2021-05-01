# 2017. 3. 13 by Hans Roh (hansroh@gmail.com)

from atila import Atila
import time
from services import cols

app = Atila (__name__)

app.mount ("/cols", cols)

@app.route ("/")
def index (was):
	return '<h1>Delune</h1>'

@app.route ("/status")
@app.permission_required (["index", "replica"])
def status (was):
	return was.status ()
