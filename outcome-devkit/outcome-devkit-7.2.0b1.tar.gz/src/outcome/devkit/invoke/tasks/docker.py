from typing import List

from invoke import Collection, Context, task

from outcome.devkit.invoke import app, docker


@task
def gcr_login(c: Context):
    """Log in to GCR."""
    info = docker.get_docker_info()
    c.run(f'cat $GOOGLE_APPLICATION_CREDENTIALS | docker login -u _json_key --password-stdin https://{info.registry}')


@task
def dockerhub_login(c: Context):
    """Log in to Dockerhub."""
    c.run('echo $DOCKER_TOKEN | docker login -u $DOCKER_USERNAME --password-stdin')


@task()
def build(c: Context):
    """Build the docker image"""
    environement = {'DOCKER_BUILDKIT': '1'}

    env_files = app.get_env_files()
    docker_info = docker.get_docker_info()

    secrets = env_files.get('secrets')

    args: List[str] = []

    if secrets is not None:
        args.extend(['--secret', f'id=build-secrets,src={secrets}'])

    args.extend(['-t', docker_info.canonical_name])
    args.extend(['-f', 'Dockerfile'])

    for key, value in docker_info.build_args:
        args.extend(['--build-arg', f'"{key}"="{value}"'])

    args.append('.')

    arg_string = ' '.join(args)
    command = f'docker build {arg_string}'

    c.run(command, env=environement)


@task()
def push(c: Context):
    """Publish the docker image"""
    info = docker.get_docker_info()
    c.run(f'docker push {info.canonical_name}')


ns = Collection(gcr_login, dockerhub_login, build, push)
