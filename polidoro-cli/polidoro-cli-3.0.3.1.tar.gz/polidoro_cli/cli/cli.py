from string import Template
from subprocess import run

import sys

from polidoro_argument import Command


class CLI:
    """
    Class to create CLI commands
    """

    @staticmethod
    def create_file_commands(full_path):
        """
        Create commands reading from file
        """
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
        run_cmd = getattr(clazz, 'get_cmd_method', CLI._get_cmd_method)(command, clazz)
        command_alias = name.replace(' ', '').split(',')
        name = command_alias.pop(0)
        # Parser full name
        setattr(run_cmd, '__qualname__', '%s.%s' % (clazz.__qualname__, name))
        # Command name
        setattr(run_cmd, '__name__', name)
        # Command class
        setattr(run_cmd, '__objclass__', clazz)
        Command(help='Run "%s"' % command, command_alias=command_alias)(run_cmd)

    @staticmethod
    def _get_cmd_method(command, clazz):
        def run_cmd_method(*_remainder, docker=False):
            docker_class = getattr(sys.modules['docker'], 'Docker', None)
            interceptors = []
            _command = command
            if docker_class and docker:
                # If the argument --docker/-d in arguments, replace "$docker" (if exists) in command
                interceptors.append(docker_class.command_interceptor)
                _command = Template(command).safe_substitute(docker='docker-compose exec $service')

            if hasattr(clazz, 'command_interceptor'):
                interceptors.append(clazz.command_interceptor)

            for interceptor in interceptors:
                _command = interceptor(_command, *_remainder)
            CLI.execute(' '.join([_command] + list(_remainder)))

        # method without "docker" argument
        def run_docker_cmd_method(*_remainder):
            run_cmd_method(*_remainder)

        if clazz.__name__ == 'Docker':
            return run_docker_cmd_method
        else:
            setattr(run_cmd_method, 'aliases', {'docker': 'd'})
            return run_cmd_method

    @staticmethod
    def execute(command, exit_on_fail=True, capture_output=False, show_cmd=True):
        """
        Run a shell command

        :param command: command as string
        :param exit_on_fail: If True, exit script if command fails
        :param capture_output: Return the command output AND not print in terminal
        :param show_cmd: Show command in terminal
        :return: subprocess.CompletedProcess
        """
        if show_cmd:
            print('+ %s' % command.strip())

        resp = run(command, shell=True, text=True, capture_output=capture_output)
        if exit_on_fail and resp.returncode:
            exit(resp)
        return resp
