import datetime
from airflow.operators.postgres_operator import PostgresOperator
from torchairflow.dag import TorchDAG
from airflow.operators.http_operator import SimpleHttpOperator


default_args = {
    'owner': 'airflow'
}


dag = TorchDAG(
    dag_id="torch_test_dag_2",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    pipeline_uid='monthly_reporting_airflow_2'
)
get_all_emps = PostgresOperator(
    task_id="get_all_emps",
    postgres_conn_id='example_db',
    sql="SELECT * FROM employee;",
    dag=dag
)

get_ip = SimpleHttpOperator(
    task_id='get_ip',
    endpoint='get',
    method='GET',
    xcom_push=True,
    dag=dag
)

get_emps_span = PostgresOperator(
        task_id="get_all_emps_3",
        postgres_conn_id='example_db',
        sql="SELECT * FROM employee;",
        dag=dag
    )

get_emps_span2 = PostgresOperator(
        task_id="get_all_emps_2",
        postgres_conn_id='example_db',
        sql="SELECT * FROM employee;",
        dag=dag
)