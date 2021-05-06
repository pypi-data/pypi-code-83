from etl_bq_tools.utils.time_execution import get_time_function_execution


@get_time_function_execution
def upload_df_to_bq(
        project_id, dataset_id, table_id, key_path,
        schema=None, df=None, if_exists="truncate", logging=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param key_path: file.json
    :param schema: dict
    :param df: Dataframe
    :param if_exists: String -> "append" or "truncate"
    :param logging: object
    :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict
    import pandas as pd

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id: {dataset_id} ')
    if not table_id:
        raise Exception('require var table_id: {table_id} ')
    if not isinstance(df, pd.DataFrame):
        raise Exception('require var df: {df} ')
    if not if_exists:
        raise Exception('require var if_exists: {if_exists} ')

    client = bigquery.Client()
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig()

    if if_exists == "truncate":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    elif if_exists == "append":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    if schema:
        job_config.schema = schema
    else:
        job_config.autodetect = True

    try:
        job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )
        job.result()
        logging.info(f"load Table {table_id} from dataframe")
    except Conflict:
        logging.info(f"Provided Schema does not match Table {table_id}")


@get_time_function_execution
def query_to_df(
        project_id=None, sql=None, file=None, use_legacy_sql=False,
        logging=None, key_path=None):
    """
    :param project_id: String
    :param sql: String
    :param file: String file_path.sql
    :param use_legacy_sql: Boolean
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not sql and not file:
        raise Exception('Required var sql or file')
    if sql and file:
        raise Exception('Only one variable is required {sql} or {file}')
    if file:
        if not str(file).endswith(".sql"):
            raise Exception('the file only support extension {file_path}.sql')

    client = bigquery.Client(project=project_id)
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    sql_text = ""
    if sql and not file:
        sql_text = sql

    if file and not sql:
        sql_text = open(file).read()

    try:
        query_config = bigquery.QueryJobConfig(use_legacy_sql=use_legacy_sql)
        df = client.query(sql_text, job_config=query_config).to_dataframe()
        logging.info("Successfully Query")
        return df
    except Exception as e:
        logging.info("Error Query")
