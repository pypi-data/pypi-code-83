import datetime
from airflow.models.baseoperator import BaseOperator
from torchairflow.utils.pipeline import get_pipeline_run


class SpanOperator(BaseOperator):
    def __init__(self, *, operator: BaseOperator, pipeline_run=None, span_uid: str = None, **kwargs):
        super().__init__(**kwargs)
        self.operator = operator
        self.pipeline_run = pipeline_run
        self.span_uid = span_uid

    def set_pipeline_run(self, pipeline_run):
        self.pipeline_run = pipeline_run

    def execute(self, context):
        try:
            print("Send span start event")
            self.pipeline_run = get_pipeline_run()
            print('pipeline run is : ', self.pipeline_run)
            self.span_context = self.pipeline_run.create_span(uid=self.span_uid,
                                                              context_data={'time': str(datetime.datetime.now())})
            self.operator.execute(context)
            context['ti'].xcom_push(key=self.span_uid, value=str(context['ti']))
        except Exception as e:
            print("Send span end failure event")
            exception = e.__dict__
            print('track back : ', e.with_traceback)
            print('----------------------------------------------------------')
            print(exception)
            self.span_context.end(
                context_data={'status': 'error', 'error_data': str(e), 'time': str(datetime.datetime.now()),
                              'exception_type': str(type(e).__name__)})
            raise e
        else:
            print("Send span end success event")
            self.span_context.end(context_data={'status': 'success', 'time': str(datetime.datetime.now())})

    def set_downstream(self, task_or_task_list) -> None:
        super().set_downstream(task_or_task_list)

    def set_upstream(self, task_or_task_list) -> None:
        super().set_upstream(task_or_task_list)
