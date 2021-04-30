ENTRYPOINT = """\
#!/bin/sh
exec /sbin/tini -- venv/bin/gunicorn --bind=0.0.0.0:8000 "--workers=$WORKERS" --worker-tmp-dir=/dev/shm "$@" {service_script}:app\
"""

DOCKERFILE = """\
FROM python:3.7-slim

# Install tini and create an unprivileged user
ADD https://github.com/krallin/tini/releases/download/v0.19.0/tini /sbin/tini
RUN addgroup --gid 1001 "elg" && adduser --disabled-password --gecos "ELG User,,," --home /elg --ingroup elg --uid 1001 elg && chmod +x /sbin/tini

# Copy in our app, its requirements file and the entrypoint script
COPY --chown=elg:elg requirements.txt docker-entrypoint.sh {required_files} /elg/
{required_folders}

# Everything from here down runs as the unprivileged user account
USER elg:elg

WORKDIR /elg

# Create a Python virtual environment for the dependencies
RUN python -mvenv venv 
RUN venv/bin/pip --no-cache-dir install -r requirements.txt 

ENV WORKERS=1

RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]\
"""

COPY_FOLDER = "COPY --chown=elg:elg {folder_name} /elg/{folder_name}/"
