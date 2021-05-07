from typing import Any, Dict, Union, Optional

from gcip.core.cache import Cache
from gcip.core.sequence import Sequence
from gcip.addons.container.jobs import dive, crane, trivy
from gcip.addons.container.config import DockerClientConfig
from gcip.addons.container.registries import Registry


def copy_container(
    *,
    src_registry: Union[Registry, str] = Registry.DOCKER,
    dst_registry: Union[Registry, str],
    image_name: str,
    image_tag: str,
    dive_kwargs: Dict[str, Any] = {},
    trivy_kwargs: Dict[str, Any] = {},
    crane_kwargs: Dict[str, Any] = {},
    docker_client_config: Optional[DockerClientConfig] = None,
    do_dive_scan: bool = True,
    do_trivy_scan: bool = True,
) -> Sequence:
    """
    Creates a `gcip.Sequence` to pull, scan and push a container image.

    The pull step is executed by `gcip.addons.container.jobs.crane.pull`, it will pull the container image an outputs it to a tarball.
    There are two scan's, optimization scan with `gcip.addons.container.jobs.dive.scan_local_image` to scan storage wasting in container image
    and a vulnerability scan with `gcip.addons.container.jobs.trivy.scan`. Both outputs are uploaded as an artifact to the GitLab instance.
    Built container image is uploaded with `gcip.addons.container.jobs.crane.push`.

    Args:
        src_registry (Union[Registry, str], optional): Container registry to pull the image from. If the container registry needs authentication,
            you have to provide a `gcip.addons.container.config.DockerClientConfig` object with credentials. Defaults to Registry.DOCKER.
        dst_registry (Union[Registry, str]): Container registry to push the image to. If the container registry needs authentication,
            you have to provide a `gcip.addons.container.config.DockerClientConfig` object with credentials. Defaults to Registry.DOCKER.
        image_name (str): Image name with stage in the registry. e.g. username/image_name.
        image_tag (str): Container image tag to pull from `src_registry` and push to `dst_registry`.
        dive_kwargs (Dict[str, Any], optional): Extra keyword arguaments passed to `gcip.addons.container.jobs.dive.scan`. Defaults to {}.
        trivy_kwargs (Dict[str, Any], optional): Extra keyword arguaments passed to `gcip.addons.container.jobs.trivy.scan_local_image`. Defaults to {}.
        crane_kwargs (Dict[str, Any], optional): Extra keyword arguaments passed to `gcip.addons.container.jobs.push`. Defaults to {}.
        docker_client_config (Optional[DockerClientConfig], optional): Creates the Docker configuration file base on objects settings,
            to authenticate against given registries. Defaults to a `DockerClientConfig` with login to the official Docker Hub
            and expecting credentials given as environment variables `REGISTRY_USER` and `REGISTRY_LOGIN`.
        do_dive_scan (Optional[bool]): Set to `False` to skip the Dive scan job. Defaults to True.
        do_trivy_scan (Optional[bool]): Set to `False` to skip the Trivy scan job. Defaults to True.

    Returns:
        Sequence: `gcip.Sequence` to pull, scan and push a container image.
    """
    job_sequence = Sequence()

    cache = Cache(paths=["image"])
    crane_pull = crane.pull(
        src_registry=src_registry,
        image_name=image_name,
        image_tag=image_tag,
        tar_path=cache.paths[0],
        docker_client_config=docker_client_config,
        **crane_kwargs,
    )
    crane_pull.set_cache(cache)
    job_sequence.add_children(crane_pull)

    if do_dive_scan:
        dive_scan = dive.scan(
            image_path=cache.paths[0],
            image_name=image_name,
            **dive_kwargs,
        )
        dive_scan.set_cache(cache)
        job_sequence.add_children(dive_scan)

    if do_trivy_scan:
        trivy_scan = trivy.scan_local_image(
            image_path=cache.paths[0],
            image_name=image_name,
            **trivy_kwargs,
        )
        trivy_scan.set_cache(cache)
        job_sequence.add_children(trivy_scan)

    crane_push = crane.push(
        dst_registry=dst_registry,
        tar_path=cache.paths[0],
        image_name=image_name,
        image_tag=image_tag,
        docker_client_config=docker_client_config,
        **crane_kwargs,
    )
    crane_push.set_cache(cache)
    job_sequence.add_children(crane_push)

    return job_sequence
