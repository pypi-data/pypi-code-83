from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import yamlarg
import sys
import os


def main():
    pkgdir = sys.modules['fast_files'].__path__[0]
    args = yamlarg.parse(os.path.join(pkgdir, 'arguments.yaml'))
    app = FastAPI()
    app.mount("/", StaticFiles(directory=args['directory']), name="static")
    uvicorn.run(app, host=args['host'], port=args['port'])