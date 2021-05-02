import json
from pathlib import Path

import yaml

from .config import print_msg


def _get_resource_name(ssm_parameter_name, prefix_to_replace):
    """
    Provide an SSM parameter name (full path) and generate a CloudFormation resource name (Logical ID)
    """  # noqa: 501
    mapping = {
        prefix_to_replace: "",
        ".": "",
        "_": " ",
        "/": " ",
        "-": " "
    }
    for key, value in mapping.items():
        ssm_parameter_name = ssm_parameter_name.replace(key, value)
    return "".join(ssm_parameter_name.title().split(" "))


def create(prefix_to_replace, replace_prefix_with,
    base_cfn_yaml_path, output_yaml_path, parameters_types_json_path, default_initial_value):  # noqa: 501
    yaml.default_flow_style = None
    parameters_yaml_doc = {
        "AWSTemplateFormatVersion": "2010-09-09",
        "Resources": {}
    }

    if not Path(parameters_types_json_path).is_file():
        raise Exception(
            "File does not exist. Run `paraman parameter-get` to generate the `.parameters_types.json` file"  # noqa : 501
        )

    with open(parameters_types_json_path, 'r') as fp:
        data = json.load(fp)

    # Handle each type of parameter differently
    for item in data['securestrings']:
        resource_name = _get_resource_name(
            item, prefix_to_replace)
        parameters_yaml_doc['Resources'][resource_name] = {
            "Type": "Custom::CfnParamStore",
            "Properties": {
                "Name": item.replace(prefix_to_replace, replace_prefix_with),
                "ServiceToken": {
                    # Required to use the Helper
                    "Fn::ImportValue": "CfnParamStore"
                },
                "Value": default_initial_value
            }
        }
    for item in data['strings']:
        resource_name = _get_resource_name(
            item, prefix_to_replace)
        parameters_yaml_doc['Resources'][resource_name] = {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Type": "String",
                "Name": item.replace(prefix_to_replace, replace_prefix_with),
                "Value": default_initial_value
            }
        }
    for item in data['stringlists']:
        resource_name = _get_resource_name(
            item, prefix_to_replace)
        parameters_yaml_doc['Resources'][resource_name] = {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Type": "StringList",
                "Name": item.replace(prefix_to_replace, replace_prefix_with),
                "Value": default_initial_value
            }
        }

    # Read base file and merge with parameters_yaml_doc
    if Path(base_cfn_yaml_path).is_file():
        with open(base_cfn_yaml_path, 'r') as fp:
            dynamic_env_yaml = yaml.safe_load(fp)
        dynamic_env_yaml['Resources'] = {
            **dynamic_env_yaml['Resources'],
            **parameters_yaml_doc['Resources']
        }
    else:
        dynamic_env_yaml = parameters_yaml_doc

    print_msg(
        f"Generated {len(parameters_yaml_doc['Resources'])} SSM Parameters resource templates"  # noqa: 501
    )

    with open(output_yaml_path, 'w') as fp:
        yaml.safe_dump(dynamic_env_yaml, fp)
        print_msg("Created the file", data=output_yaml_path)
