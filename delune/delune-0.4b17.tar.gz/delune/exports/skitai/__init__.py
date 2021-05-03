# 2017. 3. 13 by Hans Roh (hansroh@gmail.com)

import skitai
import delune
import os
import atila
import time
import sys
from .services import cols

def __config__ (pref):
	skitai.register_states (delune.SIG_UPD)
	assert pref.config.resource_dir
	pref.config.resource_dir = os.path.abspath (pref.config.resource_dir)

def __app__ ():
	app = atila.Atila (__name__)
	app.mount ("/cols", cols)

	@app.route ("/")
	def index (was):
		return '<h1>Delune</h1>'

	@app.route ("/status")
	@app.permission_required (["index", "replica"])
	def status (was):
		return was.status ()

	return app
