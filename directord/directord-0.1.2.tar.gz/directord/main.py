import argparse
import json
import os
import sys
import yaml

import tabulate

import directord
from directord import mixin
from directord import user
from directord import utils


def _args():
    """Setup client arguments."""

    parser = argparse.ArgumentParser(
        description="Deployment Framework Next.", prog="Directord"
    )
    parser.add_argument(
        "--config-file",
        help="File path for client configuration. Default: %(default)s",
        metavar="STRING",
        default=os.getenv("DIRECTOR_CONFIG_FILE"),
        type=argparse.FileType(mode="r"),
    )
    auth_group = parser.add_mutually_exclusive_group()
    auth_group.add_argument(
        "--shared-key",
        help="Shared key used for server client authentication.",
        metavar="STRING",
        default=os.getenv("DIRECTOR_SHARED_KEY"),
    )
    auth_group.add_argument(
        "--curve-encryption",
        action="store_true",
        help=(
            "Server and client will connect using Curve authentication"
            " and encryption. Enabling this option assumes keys have been"
            " generated. see `manage --generate-keys` for more."
        ),
    )
    parser.add_argument(
        "--debug",
        help="Enable debug mode. Default: %(default)s",
        action="store_true",
    )
    parser.add_argument(
        "--job-port",
        help="Job port to bind. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_MSG_PORT", 5555)),
        type=int,
    )
    parser.add_argument(
        "--transfer-port",
        help="Transfer port to bind. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_TRANSFER_PORT", 5556)),
        type=int,
    )
    parser.add_argument(
        "--heartbeat-port",
        help="heartbeat port to bind. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_HEARTBEAT_PORT", 5557)),
        type=int,
    )
    parser.add_argument(
        "--heartbeat-interval",
        help="heartbeat interval in seconds. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_HEARTBEAT_INTERVAL", 60)),
        type=int,
    )
    parser.add_argument(
        "--socket-path",
        help=(
            "Server file socket path for user interactions."
            " Default: %(default)s"
        ),
        metavar="STRING",
        default=str(
            os.getenv("DIRECTOR_SOCKET_PATH", "/var/run/directord.sock")
        ),
        type=str,
    )
    parser.add_argument(
        "--cache-path",
        help=("Client cache path." " Default: %(default)s"),
        metavar="STRING",
        default=str(os.getenv("DIRECTOR_CACHE_PATH", "/var/cache/directord")),
        type=str,
    )
    subparsers = parser.add_subparsers(
        help="Mode sub-command help", dest="mode"
    )
    parser_orchestrate = subparsers.add_parser(
        "orchestrate", help="Orchestration mode help"
    )
    parser_orchestrate.add_argument(
        "--restrict",
        help="Restrict orchestration to a set of Task SHA1(s).",
        metavar="STRING",
        nargs="+",
    )
    parser_orchestrate.add_argument(
        "--target",
        help="Worker target(s) to run a particular job against.",
        metavar="STRING",
        nargs="+",
    )
    parser_orchestrate.add_argument(
        "--ignore-cache",
        help=(
            "Instruct the orchestration engine to ignore all"
            " cache for the entirety of the run."
        ),
        action="store_true",
    )
    parser_orchestrate.add_argument(
        "--poll",
        help="Block on client return for the completion of executed jobs.",
        action="store_true",
    )
    parser_orchestrate.add_argument(
        "orchestrate_files",
        help="YAML files to use for orchestration.",
        metavar="STRING",
        nargs="+",
    )
    parser_exec = subparsers.add_parser("exec", help="Execution mode help")
    parser_exec.add_argument(
        "--verb",
        help="Module Invocation for exec. Choices: %(choices)s",
        metavar="STRING",
        choices=[
            "RUN",
            "COPY",
            "ADD",
            "ARG",
            "ENV",
            "WORKDIR",
            "CACHEFILE",
            "CACHEEVICT",
            "QUERY",
        ],
        required=True,
    )
    parser_exec.add_argument(
        "--target",
        help="Worker target(s) to run a particular job against.",
        metavar="[STRING]",
        nargs="+",
    )
    parser_exec.add_argument(
        "exec",
        help="Freeform command. Use quotes for complex commands.",
        metavar="STRING",
        nargs="+",
    )
    parser_exec.add_argument(
        "--poll",
        help="Block on client return for the completion of executed jobs.",
        action="store_true",
    )
    parser_server = subparsers.add_parser("server", help="Server mode help")
    parser_server.add_argument(
        "--bind-address",
        help="IP Address to bind a Directord Server. Default: %(default)s",
        metavar="STRING",
        default=os.getenv("DIRECTOR_BIND_ADDRESS", "*"),
    )
    parser_server.add_argument(
        "--etcd-server",
        help="Domain or IP address of the ETCD server. Default: %(default)s",
        metavar="STRING",
        default=os.getenv("DIRECTOR_ETCD_SERVER", "localhost"),
    )
    parser_server.add_argument(
        "--etcd-port",
        help="ETCD server bind port. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_ETCD_PORT", 2379)),
        type=int,
    )
    parser_server.add_argument(
        "--run-ui",
        help="Enable the Directord UI. Default: %(default)s",
        action="store_true",
    )
    parser_server.add_argument(
        "--ui-port",
        help="UI server bind port. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_UI_PORT", 9000)),
        type=int,
    )
    parser_client = subparsers.add_parser("client", help="Client mode help")
    parser_client.add_argument(
        "--server-address",
        help=(
            "Domain or IP address of the Directord server."
            " Default: %(default)s"
        ),
        metavar="STRING",
        default=os.getenv("DIRECTOR_SERVER_ADDRESS", "localhost"),
    )
    parser_manage = subparsers.add_parser(
        "manage", help="Server management mode help"
    )
    manage_group = parser_manage.add_mutually_exclusive_group(required=True)
    manage_group.add_argument(
        "--list-jobs", action="store_true", help="List all known jobs."
    )
    manage_group.add_argument(
        "--list-nodes", action="store_true", help="List all available nodes."
    )
    manage_group.add_argument(
        "--purge-jobs",
        action="store_true",
        help="Purge all jobs from the server.",
    )
    manage_group.add_argument(
        "--purge-nodes",
        action="store_true",
        help="Purge all nodes from the server.",
    )
    manage_group.add_argument(
        "--job-info",
        help="Pull information on a specific job ID.",
        metavar="STRING",
    )
    manage_group.add_argument(
        "--export-jobs",
        help="Exports all job records as YAML and dumps them to a file.",
        metavar="STRING",
    )
    manage_group.add_argument(
        "--export-nodes",
        help="Exports all node records as YAML and dumps them to a file.",
        metavar="STRING",
    )
    manage_group.add_argument(
        "--generate-keys",
        action="store_true",
        help="Generate encryption keys for Curve authentication.",
    )
    parser_bootstrap = subparsers.add_parser(
        "bootstrap",
        help=(
            "Bootstrap a directord cluster. This uses SSH to connect to remote"
            " machines and setup Directord. Once Directord is setup, SSH is no"
            " longer required."
        ),
    )
    parser_bootstrap.add_argument(
        "--catalog",
        help="File path for SSH catalog.",
        metavar="STRING",
        action="append",
        type=argparse.FileType(mode="r"),
    )
    parser_bootstrap.add_argument(
        "--key-file",
        help="SSH Key file to use when connecting to targets. Default: %(default)s",
        metavar="STRING",
        default=os.getenv(
            "DIRECTOR_BOOTSTRAP_SSH_KEY_FILE",
            os.path.join(os.environ["HOME"], ".ssh", "id_rsa"),
        ),
    )
    parser_bootstrap.add_argument(
        "--threads",
        help="Client bootstrap threads. Default: %(default)s",
        metavar="INT",
        default=int(os.getenv("DIRECTOR_BOOTSTRAP_THREADS", 10)),
        type=int,
    )
    args = parser.parse_args()
    # Check for configuration file and load it if found.
    if args.config_file:
        config_data = yaml.safe_load(args.config_file)
        for key, value in config_data.items():
            if isinstance(value, list) and key in args.__dict__:
                args.__dict__[key].extend(value)
            else:
                args.__dict__[key] = value

    return args, parser


class SystemdInstall(object):
    """Simple system service unit creation class."""

    def __init__(self):
        """Class to create systemd service units.

        This class is used with the directord-server-systemd and
        directord-client-systemd entrypoints.
        """

        self.config_path = "/etc/directord"

    def path_setup(self):
        """Create the configuration path and basic configuration file."""

        if not os.path.isdir(self.config_path):
            os.makedirs(self.config_path)
            print("[+] Created directord configuration path")

        if not os.path.exists("/etc/directord/config.yaml"):
            with open("/etc/directord/config.yaml", "w") as f:
                f.write("---\ndebug: false\n")
            print("[+] Created empty configuration file")

    def writer(self, service_file):
        """Write a given systemd service unit file.

        :param service_file: Name of the embedded service file to
                             interact with.
        :type service_file: String
        """

        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.path_setup()
        base = os.path.dirname(directord.__file__)
        service_file_path = "/etc/systemd/system/{}".format(service_file)
        if os.path.exists(service_file_path):
            print(
                "[-] Service file was not created because it already exists."
            )
            return
        with open(os.path.join(base, "static", service_file)) as f:
            with open(service_file_path, "w") as service_f:
                for line in f.readlines():
                    service_f.write(
                        line.replace(
                            "/usr/bin/directord",
                            os.path.join(path, "directord"),
                        )
                    )

        print("[+] Installed {} service unit file".format(service_file))
        print(
            "[?] Run `systemctl daemon-reload` for unit file to take effect."
        )

    def server(self):
        """Run the server systemd service unit file creation process."""

        self.writer(service_file="directord-server.service")

    def client(self):
        """Run the client systemd service unit file creation process."""

        self.writer(service_file="directord-client.service")


def _systemd_server():
    """Execute the systemd server unit file creation process."""

    _systemd = SystemdInstall()
    _systemd.server()


def _systemd_client():
    """Execute the systemd client unit file creation process."""

    _systemd = SystemdInstall()
    _systemd.client()


def main():
    """Execute the main application.

    * Server|Client operations run within the foreground of the application.

    * Exec will submit a job to be run across the cluster.

    * Manage jobs will return information about the cluster and all executed
      jobs. This data will be returned in table format for easy consumptions.
    """

    args, parser = _args()
    _mixin = mixin.Mixin(args=args)

    if args.mode == "server":
        _mixin.start_server()
    elif args.mode == "client":
        _mixin.start_client()
    elif args.mode in ["exec", "orchestrate"]:
        if args.mode == "exec":
            return_data = _mixin.run_exec()
        else:
            return_data = _mixin.run_orchestration()

        job_items = [i.decode() for i in return_data if i]

        if args.poll:
            manage = user.Manage(args=args)
            for item in job_items:
                _, status = manage.poll_job(job_id=item)
                print(status)
        else:
            for item in job_items:
                print(item)

    elif args.mode == "manage":
        manage_exec = user.Manage(args=args)
        data = manage_exec.run()
        if args.generate_keys:
            print(
                "Keys generated. Synchronize the server and client public"
                " keys to client nodes to enable Curve encryption."
            )

        if not data:
            return

        data = json.loads(data)
        if args.export_jobs or args.export_nodes:
            export_file = utils.dump_yaml(
                file_path=(args.export_jobs or args.export_nodes),
                data=dict(data),
            )
            print("Exported data to [ {} ]".format(export_file))
            return

        computed_values = dict()
        if data and isinstance(data, list):
            if args.job_info:
                headings = ["KEY", "VALUE"]

                item = dict(data).get(args.job_info)
                if not item:
                    return

                tabulated_data = _mixin.return_tabulated_info(data=item)
            else:
                restrict_headings = [
                    "EXECUTION_TIME",
                    "SUCCESS",
                    "FAILED",
                    "EXPIRY",
                ]
                _tabulated_data = _mixin.return_tabulated_data(
                    data=data, restrict_headings=restrict_headings
                )
                tabulated_data, headings, computed_values = _tabulated_data
            print(
                tabulate.tabulate(
                    [i for i in tabulated_data if i], headers=headings
                )
            )
            print("\nTotal Items: {}".format(len(tabulated_data)))
            for k, v in computed_values.items():
                if isinstance(v, float):
                    print("Total {}: {:.2f}".format(k, v))
                else:
                    print("Total {}: {}".format(k, v))
    elif args.mode == "bootstrap":
        _mixin.bootstrap_cluster()
    else:
        parser.print_help(sys.stderr)
        raise SystemExit("Mode is set to an unsupported value.")
