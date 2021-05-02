import json
from pathlib import Path

import boto3
from botocore.config import Config as botoConfig

from .config import print_msg


def get(
    parameters_region, parameters_path,
    parameters_non_recursive=False, parameters_no_decryption=False,
    parameters_max_results=1000,
    endpoint_url="",
    exclude_paths=""
):
    recursive = not parameters_non_recursive
    with_decryption = not parameters_no_decryption
    max_attempts = 10  # Hardcoded temporarily, need to pass as variable
    max_results = 10  # Hardcoded on purpose, no need to change it
    boto_config = botoConfig(
        retries={
            'max_attempts': max_attempts,
            'mode': 'standard'
        }
    )
    client_params = {
        "region_name": parameters_region,
        "config": boto_config
    }
    if endpoint_url != "":
        client_params['endpoint_url'] = endpoint_url
    client = boto3.client('ssm', **client_params)
    parameters = []
    params = {
        "Path": parameters_path,
        "Recursive": recursive,
        "WithDecryption": with_decryption,
        "MaxResults": max_results,
    }

    # Add more filters if needed
    parameter_filters = None
    # parameter_filters = [
    #     {"Key": "Label", "Option": "Equals", "Values": ["latest"]}
    # ]

    if parameter_filters:
        params = {**params, **{"ParameterFilters": parameter_filters}}
    print_msg("Request Parameters:", data=params)

    paginator = client.get_paginator('get_parameters_by_path')
    for page in paginator.paginate(**params):
        parameters += page['Parameters']
        if len(parameters) > parameters_max_results:
            break

    if exclude_paths != "":
        print_msg("Initial number of parameters", data=len(parameters))
        excluded_paths = exclude_paths.split(",")
        print_msg("Excluded paths", data=excluded_paths)
        parameters = [
            parameter for parameter in parameters
            if all(
                excluded_path not in parameter['Name'] for excluded_path in excluded_paths  # noqa: 501
            )
        ]
    print_msg("Number of parameters", data=len(parameters))
    return parameters


def put(parameters_region, parameters_json_path, prefix_to_replace, replace_prefix_with, kms_key_id, overwrite, exclude_paths, endpoint_url):  # noqa: 501

    if not Path(parameters_json_path).is_file():
        raise Exception(
            "File does not exist. Run `paraman parameter-get` to generate the `.parameters.json` file"  # noqa : 501
        )

    client_params = {
        "region_name": parameters_region,
    }
    if endpoint_url != "":
        client_params['endpoint_url'] = endpoint_url

    client = boto3.client('ssm', **client_params)

    with open(parameters_json_path, 'r') as fp:
        parameters = json.load(fp)

    if prefix_to_replace:
        for parameter in parameters:
            parameter['Name'] = parameter['Name'].replace(
                prefix_to_replace, replace_prefix_with)

    params = {
        "Tier": "Standard",
        "Overwrite": overwrite
    }
    if kms_key_id != "":
        params['KeyId'] = kms_key_id

    if exclude_paths != "":
        print_msg("Initial number of parameters", data=len(parameters))
        excluded_paths = exclude_paths.split(",")
        print_msg("Excluded paths", data=excluded_paths)
        parameters = [
            parameter for parameter in parameters
            if all(
                excluded_path not in parameter['Name'] for excluded_path in excluded_paths  # noqa: 501
            )
        ]

    responses = []
    for parameter in parameters:
        params['Name'] = parameter['Name']
        params['Type'] = parameter['Type']
        params['Value'] = parameter['Value']
        response = client.put_parameter(**params)
        print_msg(f"Parameter: {params['Name']}", data=response)
        responses.append(response)
    return responses
