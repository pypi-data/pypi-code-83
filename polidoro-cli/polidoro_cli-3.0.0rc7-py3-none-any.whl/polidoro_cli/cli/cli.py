"""
Module doc sctring
"""
# from polidoro_argument import Command

# from polidoro_cli.cli import set_environment_variables, CONFIG_FILE
import os
import re
from argparse import SUPPRESS
from string import Template

import sys
from subprocess import run

from polidoro_argument import Command


class CLI:
    """
    Class to create CLI commands
    """

    @staticmethod
    def create_file_commands(full_path):
        file = full_path.split('/')[-1]
        clazz_name = file.split('.')[0].title()
        clazz = getattr(sys.modules.get(clazz_name.lower(), None), clazz_name, None)
        if clazz is None:
            clazz = type(clazz_name, (object,), {})

        if not hasattr(clazz, 'help'):
            setattr(clazz, 'help', clazz.__qualname__ + ' CLI commands')

        with open(full_path, 'r', newline='') as file:
            for line in file.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    name, _, command = line.partition('=')
                    CLI._create_command(name, command, clazz)

    @staticmethod
    def _create_command(name, command, clazz):
        run_cmd = getattr(clazz, 'get_cmd_method', CLI.get_cmd_method)(command, clazz)
        alias = name.replace(' ', '').split(',')
        name = alias.pop(0)
        setattr(run_cmd, '__qualname__', '%s.%s' % (clazz.__qualname__, name))
        setattr(run_cmd, '__name__', name)
        setattr(run_cmd, '__objclass__', clazz)
        Command(help='Run "%s"' % command, alias=alias)(run_cmd)

    @staticmethod
    def get_cmd_method(command, clazz):
        def run_cmd_method(*_remainder, docker=False):
            docker_class = getattr(sys.modules['docker'], 'Docker', None)
            if docker_class and docker:
                docker_cmd = 'docker-compose exec $service'
            else:
                docker_cmd = ''
            _command = Template(command).safe_substitute(docker=docker_cmd)

            if docker_class and docker:
                _command = docker_class.command_interceptor(_command, *_remainder)

            if hasattr(clazz, 'command_interceptor'):
                _command = clazz.command_interceptor(_command, *_remainder)
            CLI.execute(' '.join([_command] + list(_remainder)))

        def run_docker_cmd_method(*_remainder):
            run_cmd_method(*_remainder)

        if clazz.__name__ == 'Docker':
            return run_docker_cmd_method
        else:
            setattr(run_cmd_method, 'aliases', {'docker': 'd'})
            return run_cmd_method

    @staticmethod
    def execute(command, exit_on_fail=True, capture_output=False, show_cmd=True):
        if show_cmd:
            print('+ %s' % command)
        resp = run(command, shell=True, text=True, capture_output=capture_output)
        if exit_on_fail and resp.returncode:
            exit(resp)
        return resp
    # def __init__(self, commands=None, aliases=None, helpers=None, command_help=None):
    #     if commands is None:
    #         commands = {}
    #     if aliases is None:
    #         aliases = {}
    #     if helpers is None:
    #         helpers = {}
    #     if command_help is None:
    #         command_help = {}
    #     for name, cmd in commands.items():
    #         if isinstance(cmd, dict):
    #             kwargs = cmd
    #         else:
    #             kwargs = {'cmd': cmd}
    #
    #         Command(
    #             aliases=aliases,
    #             helpers=helpers,
    #             help=command_help.get(name, 'Run "%s"' % kwargs['cmd']),
    #             method_name=name
    #         )(self.__class__.wrapper(name, **kwargs))
    #
    # @classmethod
    # def execute(cls, command, *args, docker=False, environment_vars=None, folder=None, exit_on_fail=True):
    #     if environment_vars is None:
    #         environment_vars = {}
    #     command = ' '.join([command] + list(args))
    #     if docker:
    #         from polidoro_cli.clis.docker import Docker
    #         return Docker.exec(command, environment_vars=environment_vars)
    #     else:
    #         cur_dir = os.getcwd()
    #         try:
    #             if environment_vars:
    #                 command = ' '.join(
    #                     ['%s=%s' % (name, value) for name, value in environment_vars.items()] + [command]
    #                 )
    #             print('+ %s' % command + ('' if folder is None else ' in %s' % folder))
    #             if folder:
    #                 os.chdir(folder)
    #             resp = os.system(command)
    #             if exit_on_fail and resp:
    #                 exit(resp)
    #             return resp
    #         finally:
    #             os.chdir(cur_dir)
    #
    # @staticmethod
    # @Command()
    # def set_environment_variables(*args):
    #     for env in args:
    #         key, _, value = env.partition("=")
    #         set_environment_variables(key, value, CONFIG_FILE)
