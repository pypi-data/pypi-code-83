import datetime
from airflow.models.baseoperator import BaseOperator
from torch_airflow.utils.pipeline import get_latest_pipeline_run


class SpanOperator(BaseOperator):
    def __init__(self, *, operator: BaseOperator, pipeline_uid=None, span_uid: str = None, **kwargs):
        super().__init__(**kwargs)
        self.operator = operator
        self.pipeline_uid = pipeline_uid
        self.span_uid = span_uid
        self.pipeline_run = None
        self.span_context = None

    def set_pipeline_run(self, pipeline_run):
        self.pipeline_run = pipeline_run

    def execute(self, context):
        try:
            print("Sending Span Start Event")
            self.pipeline_run = get_latest_pipeline_run(self.pipeline_uid)
            self.span_context = self.pipeline_run.create_span(uid=self.span_uid,
                                                              context_data={'time': str(datetime.datetime.now())})
            self.operator.execute(context)
            context['ti'].xcom_push(key=self.span_uid, value=str(context['ti']))
        except Exception as e:
            print("Sending Span End Event With Status Failure")
            exception = e.__dict__
            print(exception)
            self.span_context.end(
                context_data={'status': 'error', 'error_data': str(e), 'time': str(datetime.datetime.now()),
                              'exception_type': str(type(e).__name__)})
            raise e
        else:
            print("Sending Span End Event With Status Success")
            self.span_context.end(context_data={'status': 'success', 'time': str(datetime.datetime.now())})

    def set_downstream(self, task_or_task_list) -> None:
        super().set_downstream(task_or_task_list)

    def set_upstream(self, task_or_task_list) -> None:
        super().set_upstream(task_or_task_list)
