"""Sub-command of `hdev` to clean projects."""
import os
import subprocess

from pkg_resources import resource_filename

from hdev.command.sub_command import SubCommand
from hdev.configuration import load_configuration


class Clean(SubCommand):
    """Sub-command of `hdev` to print out python version information."""

    name = "clean"
    help = "Clean a project directory"

    DEFAULT_CLEAN = {
        "files": ["node_modules/.uptodate", ".coverage"],
        "dirs": [
            "build",
            "build.eggs",
            "dist",
            "*.egg-info",
            "src/*.egg-info",
            ".coverage.*",
            ".pytest_cache",
        ],
        "file_names": ["*.py[co]"],
        "dir_names": ["__pycache__"],
    }
    DEEP_CLEAN = {"dirs": [".tox", "node_modules"]}

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument(
            "--all",
            "-a",
            action="store_true",
            help="Clean everything we know how to clean.",
        )

        parser.add_argument(
            "--deep",
            "-d",
            action="store_true",
            help="Clean items which might be slow to rebuild like tox and node modules",
        )

        parser.add_argument(
            "--branches",
            "-b",
            action="store_true",
            help="Clean and prune old and detached git branches as well",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        os.chdir(args.project_dir)

        # Merge any project specific settings with our defaults
        config = load_configuration(args.project_file).get("tool.hdev.clean", {})
        to_clean = dict(self.DEFAULT_CLEAN)
        for key in to_clean:
            to_clean[key].extend(config.get(key, []))

        self._clean(**to_clean, verbose=args.debug)

        if args.deep or args.all:
            self._clean(**self.DEEP_CLEAN, verbose=args.debug)

        if args.branches or args.all:
            self._run_script("clean_branches.sh")

    @classmethod
    def _clean(
        # pylint: disable=too-many-arguments
        cls,
        files=None,
        dirs=None,
        file_names=None,
        dir_names=None,
        verbose=False,
    ):
        script_lines = []
        for options, items in (("--force", files), ("--recursive --force", dirs)):
            if verbose:
                options += " --verbose"
            if items:
                script_lines.append(f"rm {options} {' '.join(items)}")

        if file_names:
            name_selector = " -or ".join([f'-name "{item}"' for item in file_names])

            script_lines.append(f"find . -type f \\( {name_selector} \\) -delete")

        if dir_names:
            name_selector = " -or ".join([f'-name "{item}"' for item in dir_names])

            rm_command = "rm --recursive"
            if verbose:
                rm_command += " --verbose"

            script_lines.append(
                f"find . -type d \\( {name_selector} \\) -exec {rm_command} {{}} +"
            )

        script_content = ";".join(script_lines)

        subprocess.check_call(script_content, shell=True)

    @classmethod
    def _run_script(cls, script_name):
        script = resource_filename("hdev", f"resources/bin/{script_name}")

        subprocess.check_call([script])
