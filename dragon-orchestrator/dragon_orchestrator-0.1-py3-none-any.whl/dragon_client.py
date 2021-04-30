import datetime

import docker


def get_client_instance():
    """
    Get the docker client instance
    """
    return docker.from_env()


def start_container(image, name, command=None, port_mappings=None):
    """
    Start a container on the client
    """
    container = get_client_instance().containers.run(
        image, command=command, detach=True, name=name, ports=port_mappings
    )
    return container.id


def commit_container(container_id, repository, tag="latest"):
    """
    Commit a container
    """
    container = get_client_instance().containers.get(container_id)
    container.commit(
        repository=repository,
        tag=tag,
        message="Commited by dragon orchestrator service on {}"
        % str(datetime.datetime.now()),
    )


def stop_container(container_id):
    """
    Stop a container if its running.
    """
    container = get_client_instance().containers.get(container_id)
    container.stop()


def remove_container(container_id, force=True):
    """
    Remove a container
    """
    container = get_client_instance().containers.get(container_id)
    container.remove(force=force)
