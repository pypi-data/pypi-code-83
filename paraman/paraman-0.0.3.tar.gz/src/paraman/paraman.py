import json

import click

from .config import is_docker, pass_config, json_serial
from .cloudformation import create as create_cloudformation
from .parameters import get as get_parameters
from .parameters import put as put_parameters


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        app_aliases = {
            "p": "parameter",
            "c": "cloudformation"
        }
        action_aliases = {
            "a": "apply",
            "c": "create",
            "d": "delete",
            "g": "get",
            "l": "list",
            "p": "put",
            "r": "reload",
            "s": "start"
        }
        if len(cmd_name) == 2:
            words = []
            if cmd_name[0] in app_aliases:
                words.append(app_aliases[cmd_name[0]])
            if cmd_name[1] in action_aliases:
                words.append(action_aliases[cmd_name[1]])
            if len(words) == 2:
                cmd_name = "-".join(words)

        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")


@click.command(cls=AliasedGroup)
@pass_config
@click.option(
    '--ci', '-ci',
    is_flag=True, help="Use this flag to avoid confirmation prompts"
)
@click.option(
    '--local-dev', '-dev',
    is_flag=True, help="Use this flag for local tests with localstack"
)
@click.option(
    '--endpoint-url', '-u',
    required=False,
    default="",
    type=str,
    help="Set a custom AWS endpoint_url"
)
def cli(config, ci, local_dev, endpoint_url):
    """
Examples:

paraman --parameters-region eu-west-1 parameter-get              \\                                             
--prefix-to-replace /my-app/development/                         \\                        
--exclude-paths "/accounts/,/google_credentials/,/cookie_secret"


paraman cloudformation-create                                    \\                                  
--prefix-to-replace /my-app/development/                         \\                        
--replace-prefix-with /my-app/test/


aws cloudformation deploy                                        \\                      
--region us-east-1                                               \\                
--template-file .merged.yaml                                     \\                                
--stack-name test-virginia


paraman --parameters-region us-east-1 parameter-put              \\                                            
--prefix-to-replace /my-app/dev/                                 \\                            
--replace-prefix-with /my-app/test/                              \\                                     
--overwrite=true
"""  # noqa: 501

    if is_docker():
        ci = True
    config.ci = ci
    config.local_dev = local_dev
    config.endpoint_url = endpoint_url
    if local_dev and endpoint_url == "":
        config.endpoint_url = "http://localhost:4566"


@cli.command()
@pass_config
@click.option(
    '--parameters-region', '-r',
    prompt=True, required=False, type=str, envvar='PARAMAN_AWS_REGION')
@click.option(
    '--parameters-path', '-p',
    default='/',
    prompt=True, required=False, show_default=True, type=str,
    envvar='PARAMAN_PARAMETERS_PATH'
)
@click.option(
    '--non-recursive',
    default=False,
    prompt=False, required=False, show_default=True, type=bool,
)
@click.option(
    '--no-decryption',
    default=False,
    prompt=False, required=False, show_default=True, type=bool,
)
@click.option(
    '--max-results', '-m',
    default=1000,
    prompt=False, required=False, show_default=True, type=int,
)
@click.option(
    '--exclude-paths', '-e',
    default="",
    help="If a parameter's path contains one of the Comma delimited strings, exclude it",  # noqa: 501
    prompt=False, required=False, show_default=True, type=str,
)
def parameter_get(
    config,
    parameters_region, parameters_path,
    non_recursive, no_decryption, max_results,
    exclude_paths,
):
    """Alias: pg\n
Gets `parameters_region` and `parameters_path`\n
Returns a list object, and generates `.parameters.json` and `.parameters_types.json`\n
`.parameters.json` - list of parameters including values.\n
`.parameters_types.json` - dictionary of parameter types, each parameter type contains a list of parameters names.\n
"""  # noqa: 501
    parameters = get_parameters(parameters_region, parameters_path,
                                non_recursive, no_decryption, max_results,
                                config.endpoint_url, exclude_paths)
    with open('.parameters.json', 'w') as fp:
        json.dump(parameters, fp, indent=2,
                  sort_keys=True, default=json_serial)
    types = {
        "securestrings": [
            p["Name"] for p in parameters if p["Type"] == "SecureString"
        ],
        "strings": [
            p["Name"] for p in parameters if p["Type"] == "String"
        ],
        "stringlists": [
            p["Name"] for p in parameters if p["Type"] == "Stringlist"
        ]
    }

    with open('.parameters_types.json', 'w') as fp:
        json.dump(types, fp, indent=2, sort_keys=True, default=json_serial)


@cli.command()
@pass_config
@click.option(
    '--parameters-region', '-r',
    prompt=True, required=False, type=str, envvar='PARAMAN_AWS_REGION')
@click.option(
    '--parameters-json-path', '-j',
    default='.parameters.json',
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_PARAMETERS_JSON_PATH',
)
@click.option(
    '--prefix-to-replace', '-s',
    default="",
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_PREFIX_TO_REPLACE',
)
@click.option(
    '--replace-prefix-with', '-d',
    default="",
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_REPLACE_PREFIX_WITH',
)
@click.option(
    '--kms-key-id', '-k',
    default="",
    prompt=False, required=False, show_default=True, type=str,
)
@click.option(
    '--overwrite', '-o',
    default=False,
    help="Overwrites parameters values if exist",  # noqa: 501
    prompt=False, required=False, show_default=True, type=bool,
)
@click.option(
    '--exclude-paths', '-e',
    default="",
    help="If a parameter's path contains one of the Comma delimited strings, exclude it",  # noqa: 501
    prompt=False, required=False, show_default=True, type=str,
)
def parameter_put(
    config,
    parameters_region, parameters_json_path,
    prefix_to_replace, replace_prefix_with,
    kms_key_id, overwrite, exclude_paths,
):
    """Alias: pp\n
Gets `parameters_region` and `parameters_path`\n
Puts parameter values in AWS according to `parameters_json_path`\n
Returns a list of responses \n
"""  # noqa: 501
    responses = put_parameters(
        parameters_region, parameters_json_path, prefix_to_replace,
        replace_prefix_with, kms_key_id, overwrite, exclude_paths,
        config.endpoint_url
    )
    return responses


@cli.command()
@pass_config
@click.option(
    '--prefix-to-replace', '-s',
    default="",
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_PREFIX_TO_REPLACE',
)
@click.option(
    '--replace-prefix-with', '-d',
    default="",
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_REPLACE_PREFIX_WITH',
)
@click.option(
    '--base-cfn-yaml-path', '-f',
    default="",
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_BASE_CFN_YAML_PATH',
)
@click.option(
    '--output-yaml-path', '-o',
    default='.merged.yaml',
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_OUTPUT_YAML_PATH',
)
@click.option(
    '--parameters-types-json-path', '-j',
    default='.parameters_types.json',
    prompt=False, required=False, show_default=True, type=str,
    envvar='PARAMAN_PARAMETERS_TYPES_JSON_PATH',
)
@click.option(
    '--default-initial-value', '-v',
    default='empty',
    prompt=False, required=False, show_default=True,
    envvar='PARAMAN_DEFAULT_INITIAL_VALUE',
)
def cloudformation_create(
    config,
    prefix_to_replace, replace_prefix_with,
    base_cfn_yaml_path, output_yaml_path,
    parameters_types_json_path,
    default_initial_value
):
    """Alias: cc\n
Gets SSM Parameters from AWS or from the local file `.parameters_types.json`\n
Generates a CloudFormation resource template per SSM parameter and merges to the file `base_cfn_yaml_path`.\n
If `base_cfn_yaml_path` is empty, then the file `output_yaml_path` will contain a deployable CloudFormation template.
"""  # noqa: 501
    create_cloudformation(
        prefix_to_replace, replace_prefix_with,
        base_cfn_yaml_path, output_yaml_path,
        parameters_types_json_path,
        default_initial_value
    )


@ cli.command()
def version():
    """Print the installed version"""
    from .__init__ import __version__ as version
    from .__init__ import __short_commit__ as short_commit

    if version == "99.99.99":
        version = "docker"
    elif version == "0.0.1":
        version = "local"

    if short_commit == "abcd123":
        short_commit = "unknown_commit_hash"

    msg = f"{version} {short_commit}"
    print(msg)
