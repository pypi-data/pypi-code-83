from torch_airflow.utils.pipeline import get_latest_pipeline_run
from torchsdktest.models.pipeline import PipelineRunResult, PipelineRunStatus


# update pipeline with success status
def on_dag_failure_callback(context):
    pipeline_uid = context['dag'].__dict__['pipeline_uid']
    pipeline_run = get_latest_pipeline_run(pipeline_uid)
    pipeline_run.update_pipeline_run(
        context_data={'status': 'failure', 'dag': 'torch_dag', 'context': str(context)},
        result=PipelineRunResult.FAILURE,
        status=PipelineRunStatus.FAILED
    )


# update pipeline with failed status
def on_dag_success_callback(context):
    pipeline_uid = context['dag'].__dict__['pipeline_uid']
    pipeline_run = get_latest_pipeline_run(pipeline_uid)
    pipeline_run.update_pipeline_run(
        context_data={'status': 'success', 'dag': 'torch_dag', 'context': str(context)},
        result=PipelineRunResult.SUCCESS,
        status=PipelineRunStatus.COMPLETED
    )
