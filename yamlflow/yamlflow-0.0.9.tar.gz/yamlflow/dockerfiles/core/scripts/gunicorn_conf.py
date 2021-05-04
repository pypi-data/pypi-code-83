import json
import multiprocessing
import os


host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8000")
bind_env = os.getenv("BIND", None)
use_loglevel = os.getenv("LOG_LEVEL", "info")
if bind_env:
    use_bind = bind_env
else:
    use_bind = f"{host}:{port}"

web_concurrency_env = os.getenv("WEB_CONCURRENCY", None)
web_concurrency_max = 2 * multiprocessing.cpu_count() + 1
web_concurrency_min = 1
default_web_concurrency = web_concurrency_min
if web_concurrency_env:
    web_concurrency = int(web_concurrency_env)
else:
    web_concurrency = default_web_concurrency

accesslog_var = "-" # to stdout, other option is to file
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(q)s %(s)s %(b)s "%(a)s" "%(T)s"'
use_accesslog = accesslog_var or None
errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None
graceful_timeout_str = os.getenv("GRACEFUL_TIMEOUT", "300")
timeout_str = os.getenv("TIMEOUT", "300")
keepalive_str = os.getenv("KEEP_ALIVE", "5")

# Gunicorn config variables
loglevel = use_loglevel
workers = web_concurrency
bind = use_bind
errorlog = use_errorlog
worker_tmp_dir = "/dev/shm"
accesslog = use_accesslog
graceful_timeout = int(graceful_timeout_str)
timeout = int(timeout_str)
keepalive = int(keepalive_str)


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    # Additional, non-gunicorn variables
    "host": host,
    "port": port,
}
print(json.dumps(log_data))
