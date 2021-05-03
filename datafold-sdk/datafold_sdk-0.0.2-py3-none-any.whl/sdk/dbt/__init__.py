import logging
import os
import tempfile
import zipfile

from datafold.sdk.exceptions import DatafoldSDKException
from datafold.sdk.utils import prepare_api_url, prepare_headers, run_command, post_data

logger = logging.getLogger(__file__)


def check_commit_sha(cwd):
    logging.info(f"Attempting to resolve commit-sha in directory: {cwd}")
    # Attempt to resolve commit sha from git command
    commit_sha = run_command(["git", "rev-parse", "HEAD"], capture=True, cwd=cwd)
    logging.info(f"Found commit sha: {commit_sha}")
    return commit_sha


def submit_artifacts(host: str,
                     api_key: str,
                     ci_config_id: int,
                     run_type: str,
                     target_folder: str,
                     commit_sha: str = None):
    """
    Submits dbt artifacts to the datafold app server.

    Args:
        host          (str): The location of the datafold app server.
        api_key       (str): The API_KEY to use for authentication
        ci_config_id  (int): The ID of the CI config for which you submit these artefacts
                             (See the CI config ID in the CI settings screen).
        run_type      (str): The run_type to apply. Can be either "pull_request" or "production"
        target_folder (str): The location of the `target` folder after the `dbt run`, which includes
                             files this utility will zip and include in the upload
        commit_sha    (str): Optional. If not provided, the SDK will resolve this through a git command
                             otherwise used as is.
    Returns:
        None
    """

    api_segment = f"api/v1/dbt/submit_artifacts/{ci_config_id}"
    url = prepare_api_url(host, api_segment)
    headers = prepare_headers(api_key)

    if not commit_sha:
        commit_sha = check_commit_sha(target_folder)

    if not commit_sha:
        logging.error("No commit sha resolved. Override the commit_sha with the --commit-sha parameter")
        raise DatafoldSDKException("No commit sha resolved")

    target_folder = os.path.abspath(target_folder)
    with tempfile.NamedTemporaryFile(suffix=".zip", mode='w+b', delete=True) as tmp_file:
        zip_file = zipfile.ZipFile(tmp_file.name, 'w')

        seen_manifest = False
        seen_results = False
        for folder_name, subfolders, file_names in os.walk(target_folder):
            rel_path = os.path.relpath(folder_name, target_folder)
            for file_name in file_names:
                if file_name == "manifest.json":
                    seen_manifest = True
                if file_name == "run_results.json":
                    seen_results = True

                file_path = os.path.join(folder_name, file_name)
                zip_path = os.path.join(rel_path, os.path.basename(file_path))
                zip_file.write(file_path, zip_path)

        zip_file.close()

        if not seen_manifest or not seen_results:
            logging.error("The manifest.json or run_results.json is missing in the target directory.")
            raise DatafoldSDKException("The manifest.json or run_results.json is missing in the target directory.")

        files = {'artifacts': open(tmp_file.name, 'rb')}
        data = {'commit_sha': commit_sha, 'run_type': run_type}

        post_data(url, files=files, data=data, headers=headers)

    logging.info("Successfully uploaded the manifest")
