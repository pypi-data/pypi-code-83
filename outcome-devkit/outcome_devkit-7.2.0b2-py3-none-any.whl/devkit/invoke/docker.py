"""Docker helpers."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterator, List, Optional, Sequence, Tuple, cast

from invoke import Context, Result
from pydantic import BaseModel, Field, validator

from outcome.devkit.invoke import app

EnvironmentVar = Dict[str, str]
CommandArgs = Sequence[Tuple[str, ...]]
Volumes = Sequence[Tuple[str, str]]


class UnknownContainer(Exception):
    ...


class DuplicateContainer(Exception):
    ...


default_args = ['--rm']


def create_container(  # noqa: WPS211, WPS231
    c: Context,
    name: str,
    image: str,
    environment: Optional[EnvironmentVar] = None,
    port: Optional[int] = None,
    workdir: Optional[str] = None,
    volumes: Optional[Volumes] = None,
    detach: bool = True,
    additional_args: Optional[List[str]] = None,
    command: Optional[str] = None,
    command_args: Optional[CommandArgs] = None,
    command_args_sep: str = ' ',
):
    environment = environment or {}
    volumes = volumes or []
    additional_args = additional_args or []

    if container_exists(c, name):
        raise DuplicateContainer(name)

    args = default_args.copy()

    args.append(f'--name {name}')

    if detach:
        args.append('-d')
    else:
        args.append('-it')

    if workdir:
        args.append(f'-w {workdir}')

    for volume in volumes:
        args.append(f'-v {volume[0]}:{volume[1]}')

    if port:
        args.append(f'-p {port}:{port}')

    for key, value in environment.items():
        args.append(f'-e {key}="{value}"')

    arg_string = ' '.join(args + additional_args)

    command_to_run = f'docker run {arg_string} {image}'

    if command:
        command_to_run = f'{command_to_run} {command}'

        if command_args:
            for command_arg in command_args:
                command_arg_string = command_args_sep.join(command_arg)
                command_to_run = f'{command_to_run} {command_arg_string}'

    c.run(command_to_run)


def start_container(c: Context, name: str):
    if not container_exists(c, name):
        raise UnknownContainer

    if not container_is_running(c, name):
        c.run(f'docker start {name}')


def stop_container(c: Context, name: str):
    if container_is_running(c, name):
        c.run(f'docker stop {name}')


class DockerState(Enum):
    running = 'running'
    exited = 'exited'


class DockerProcess(BaseModel):
    class Config:
        extra = 'ignore'

    command: str = Field(..., alias='Command')
    identifier: str = Field(..., alias='ID')
    image: str = Field(..., alias='Image')
    state: DockerState = Field(..., alias='State')
    names: List[str] = Field(..., alias='Names')

    @validator('names', pre=True)
    def parse_list(cls, v: object) -> object:  # noqa: N805  # pragma: no cover
        if isinstance(v, str):
            return v.split(',')
        return v


def container_exists(c: Context, name: str) -> bool:
    for container in get_docker_containers(c, only_running=False):
        if name in container.names:
            return True

    return False


def container_is_running(c: Context, name: str) -> bool:
    for container in get_docker_containers(c):
        if name in container.names:
            return container.state == DockerState.running

    return False


def get_docker_containers(c: Context, only_running: bool = True) -> Iterator[DockerProcess]:
    options: List[str] = ["--format '{{json .}}'"]

    if only_running:
        options.append('-a')

    opts = ' '.join(options)
    command = f'docker ps {opts}'

    res = cast(Result, c.run(command, echo=False, hide=True))
    output = cast(str, res.stdout)

    yield from (DockerProcess.parse_raw(line) for line in output.splitlines() if line)


@dataclass
class DockerInfo:  # pragma: no cover
    tag: str
    name: str
    registry: str
    repository: str
    build_args: Sequence[Tuple[str, str]]

    @property
    def image(self) -> str:
        return f'{self.repository}/{self.name}:{self.tag}'

    @property
    def canonical_name(self) -> str:
        return f'{self.registry}/{self.image}'


def get_docker_info() -> DockerInfo:  # pragma: no cover
    app_info = app.get_app_info()
    git_info = app.get_git_info()

    docker_registry = app.project_config.get('TOOL_DOCKER_REGISTRY')
    docker_repository = app.project_config.get('TOOL_DOCKER_REPOSITORY')

    assert isinstance(docker_registry, str) and isinstance(docker_repository, str)

    tag = app_info.version

    if git_info is not None and not git_info.is_master:
        tag = f'{tag}-{git_info.normalized_branch}'

    build_args: List[Tuple[str, str]] = []

    build_args.append(('APP_VERSION', app_info.version))
    build_args.append(('APP_NAME', app_info.name))

    if app_info.port is not None:
        build_args.append(('APP_PORT', str(app_info.port)))

    return DockerInfo(tag, app_info.name, docker_registry, docker_repository, build_args)
