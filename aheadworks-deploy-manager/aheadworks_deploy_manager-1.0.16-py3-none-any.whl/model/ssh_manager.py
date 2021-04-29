import subprocess


class SshManager:

    def run_ssh_command(self, command, host, user):
        host = user + '@' + host

        try:
            output = subprocess.check_output(
                ["ssh", "%s" % host, command],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            output = output.splitlines()
        except Exception:
            output = []

        return output
