import datetime
from airflow.operators.postgres_operator import PostgresOperator
from torchsdktest.models.pipeline import PipelineRunResult, PipelineRunStatus
from torchairflow.dag import TorchDAG
# from torchairflow.utils.callback import on_dag_failure_callback, on_dag_success_callback

default_args = {
    'owner': 'airflow'
}

dag = TorchDAG(
    dag_id="torch_pkg_dag_test",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    pipeline_uid='monthly_reporting_airflow'
)

get_emps = PostgresOperator(
    task_id="get_emps",
    postgres_conn_id='example_db',
    sql="SELECT * FROM employee;",
    dag=dag
)

insert_emps = PostgresOperator(
    task_id="insert_into_empployee_table",
    postgres_conn_id='example_db',
    sql="""
        INSERT INTO  employee( "name", emp_type, birth_date, company) VALUES ( 'Vaishvik', 'SDE', '2018-07-05', 'Acceldata');
    """,
    dag=dag
)

get_emps_new = PostgresOperator(
    task_id="get_ad_emps",
    postgres_conn_id='example_db',
    sql="SELECT * FROM employee;",
    dag=dag
)

dag.set_dependency(insert_emps, get_emps)
dag.set_dependency(get_emps, get_emps_new)
