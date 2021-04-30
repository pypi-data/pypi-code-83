import os

from enum import Enum
from datetime import timedelta
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
from airflow.contrib.operators import kubernetes_pod_operator
from knada_composer_wrappers.init_containers import create_read_bucket_init_container


class DBTCommand(Enum):
    DEBUG = "debug"
    TEST = "test"
    RUN = "run"


def create_dbt_pod_operator(
    task_id: str,
    bucket_dbt_path: str,
    dbt_cmd: DBTCommand = DBTCommand.DEBUG,
    delete_on_completed: bool = True,
    retries: int = 1,
    retry_delay: timedelta = timedelta(seconds=5),
    namespace: str = "default",
):
    return kubernetes_pod_operator.KubernetesPodOperator(
        init_containers=[create_read_bucket_init_container(bucket_dbt_path)],
        task_id=task_id,
        name=task_id,
        cmds=["dbt", dbt_cmd.value],
        arguments=["--profiles-dir", "/data", "--project-dir", "/data"],
        env_vars={"REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt"},
        namespace=namespace,
        volume_mounts=[
            VolumeMount(
                name="data", mount_path="data", sub_path=None, read_only=False
            )
        ],
        startup_timeout_seconds=360,
        volumes=[Volume(name="data", configs={})],
        image=os.getenv("KNADA_DBT_IMAGE", "navikt/knada-dbt:4"),
        retries=retries,
        retry_delay=retry_delay,
        is_delete_operator_pod=delete_on_completed,
    )


def create_python_pod_operator(
    task_id: str,
    python_cmd: str,
    bucket_path: str = None,
    extra_envs: dict = None,
    delete_on_completed: bool = True,
    retries: int = 1,
    retry_delay: timedelta = timedelta(seconds=5),
    namespace: str = "default",
):

    envs = {"REQUESTS_CA_BUNDLE": "/etc/ssl/certs/ca-certificates.crt"}

    if extra_envs:
        envs = dict(envs, **extra_envs)

    return kubernetes_pod_operator.KubernetesPodOperator(
        init_containers=[create_read_bucket_init_container(bucket_path)] if bucket_path else None,
        task_id=task_id,
        name=task_id,
        cmds=["python", "-c"],
        arguments=[python_cmd],
        env_vars=envs,
        namespace=namespace,
        volume_mounts=[
            VolumeMount(
                name="data", mount_path="data", sub_path=None, read_only=False
            )
        ],
        startup_timeout_seconds=360,
        volumes=[Volume(name="data", configs={})],
        image=os.getenv("KNADA_PYTHON_IMAGE", "navikt/dataprodukt-poc:v6"),
        retries=retries,
        retry_delay=retry_delay,
        is_delete_operator_pod=delete_on_completed,
    )
