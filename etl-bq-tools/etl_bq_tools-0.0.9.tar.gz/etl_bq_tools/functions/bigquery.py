from etl_bq_tools.utils.time_execution import get_time_function_execution


@get_time_function_execution
def bq_create_dataset(project_id=None,
                      dataset_id=None,
                      logging=None,
                      key_path=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param key_path: file.json
    :param logging: object
    :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    dataset_id = f"{project_id}.{dataset_id}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"

    try:
        dataset = client.create_dataset(dataset, exists_ok=True)
        logging.info(f"Created dataset {project_id}.{dataset.dataset_id}")
    except Conflict:
        logging.info(f"Already Exists or ProjectID Not Found {project_id}.{dataset.dataset_id}")


@get_time_function_execution
def bq_delete_dataset(project_id=None,
                      dataset_id=None,
                      logging=None,
                      key_path=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery
    from google.cloud.exceptions import Conflict

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    dataset_id = f"{project_id}.{dataset_id}"

    try:
        client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
        logging.info("Deleted dataset '{}'.".format(dataset_id))
    except Conflict:
        logging.info(f"Dataset Not Found {project_id}.{dataset_id}")


@get_time_function_execution
def bq_list_dataset(project_id=None,
                    logging=None,
                    key_path=None):
    """
    :param project_id: String
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    datasets = list(client.list_datasets())

    data_list = list()
    if datasets:
        logging.info(f"Datasets in project {project_id}:")
        for dataset in datasets:
            data_dict = dict()
            data_dict["project_id"] = dataset.project
            data_dict["dataset_id"] = dataset.dataset_id
            data_list.append(data_dict)
            print(f"\t {dataset.project}.{dataset.dataset_id}")
    else:
        logging.info(f"{project_id} project does not contain any datasets.")

    return data_list


@get_time_function_execution
def bq_create_table(project_id=None,
                    dataset_id=None,
                    table_id=None,
                    schema=None,
                    logging=None,
                    key_path=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param schema: dict
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id: {dataset_id} ')
    if not table_id:
        raise Exception('require var table_id: {table_id} ')
    if not schema:
        raise Exception('require var schema ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{project_id}.{dataset_id}.{table_id}"
    table = bigquery.Table(table_id, schema=schema)

    try:
        table = client.create_table(table)
        logging.info(f"Created Table {table.project}.{table.dataset_id}.{table.table_id}")
    except Conflict:
        logging.info(f"Already Exists or TableID Not Found {table.project}.{table.dataset_id}.{table.table_id}")


@get_time_function_execution
def bq_delete_table(project_id=None,
                    dataset_id=None,
                    table_id=None,
                    logging=None,
                    key_path=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')
    if not table_id:
        raise Exception('require var table_id: {table_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    table_id = f"{project_id}.{dataset_id}.{table_id}"
    try:
        client.delete_table(table_id, not_found_ok=True)
        logging.info("Deleted table '{}'.".format(table_id))
    except Conflict:
        logging.info(f"Table Not Found {project_id}.{dataset.dataset_id}")


@get_time_function_execution
def bq_list_tables(project_id=None,
                   dataset_id=None,
                   logging=None,
                   key_path=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery

    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id:{dataset_id} ')

    client = bigquery.Client(project=project_id)
    if project_id and key_path:
        client = bigquery.Client.from_service_account_json(key_path)

    dataset_id = f"{project_id}.{dataset_id}"
    tables = client.list_tables(dataset_id)

    data_list = list()

    if tables:
        logging.info("Tables contained in '{}':".format(dataset_id))
        for table in tables:
            data_dict = dict()
            data_dict["project_id"] = table.project
            data_dict["dataset_id"] = table.dataset_id
            data_dict["table_id"] = table.table_id
            data_list.append(data_dict)
            print(f"\t {table.project}.{table.dataset_id}.{table.table_id}")
    else:
        logging.info(f"{project_id}.{dataset_id} dataset does not contain any tables.")
    return data_list


@get_time_function_execution
def bq_copy_table(orig_table_id=None,
                  dest_table_id=None,
                  logging=None,
                  key_path=None):
    """
    :param orig_table_id: String {project_id}.{dataset_id}.{table_id}
    :param dest_table_id: String {project_id}.{dataset_id}.{table_id}
    :param logging: object
    :param key_path: file.json
    :return:
    """
    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict

    if not orig_table_id:
        raise Exception('require var orig_table_id: {project_id}.{dataset_id}.{table_id} ')
    if not dest_table_id:
        raise Exception('require var dest_table_id: {project_id}.{dataset_id}.{table_id} ')

    client = bigquery.Client()
    if key_path:
        client = bigquery.Client.from_service_account_json(key_path)
    job_config = bigquery.CopyJobConfig()
    try:
        job = client.copy_table(orig_table_id, dest_table_id, job_config=job_config)
        job.result()
        logging.info(f"Copy Table {orig_table_id} from {dest_table_id}  ")
    except Conflict:
        logging.info(f"Table Not Found")


@get_time_function_execution
def bq_query_to_df(
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
