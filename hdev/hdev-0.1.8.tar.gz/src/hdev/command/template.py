import json

from hdev.command import SubCommand
from hdev.cookie_cutter import CookieCutter


class Template(SubCommand):
    """Sub-command of `hdev` to print out python version information."""

    name = "template"
    help = "Update the local project template"

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """

        config_file = args.project_dir / ".cookiecutter.json"
        if not config_file.exists():
            print("This does not look like a cookie cutter project.")
            return

        with open(config_file) as handle:
            config = json.load(handle)

        project_name = CookieCutter.replay(project_dir=args.project_dir, config=config)

        template = CookieCutter.get_template_from_config(config)
        print(f"Recreated {project_name} from {template}")
        print("You should now check for updated files...")
