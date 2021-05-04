def upload_df_to_bq(
        project_id, dataset_id, table_id, service_account,
        schema=None, df=None, if_exists="truncate", logging=None):
    """
    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param service_account: file.json
    :param schema: dict
    :param df: Dataframe
    :param if_exists: String -> "append" or "truncate"
    :param logging: object
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
    if not df:
        raise Exception('require var df: {df} ')
    if not if_exists:
        raise Exception('require var if_exists: {if_exists} ')

    client = bigquery.Client()
    if service_account:
        client = bigquery.Client.from_service_account_json(service_account)

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


def upload_uri_to_bq(
        project_id, dataset_id, table_id, service_account,
        schema=None, uri=None, if_exists="truncate",
        file_format=None, logging=None, delimiter=',', quotechar='"',
        encoding=None, skip_leading_rows=0):
    """
    :param project_id: String
    :param dataset_id: String
    :param table_id: String
    :param service_account: file.json
    :param schema: dict
    :param uri:  gs://
    :param if_exists: String -> append or truncate
    :param file_format: String -> parquet,avro, orc, json
    :param logging: object
    :param delimiter: String -> Default: ','
    :param quotechar: String -> Default: '""'
    :param encoding: String
    :param skip_leading_rows: Integer
    :return:
    """

    from google.cloud import bigquery
    from google.api_core.exceptions import Conflict

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    if not dataset_id:
        raise Exception('require var dataset_id: {dataset_id} ')
    if not table_id:
        raise Exception('require var dataset_id: {dataset_id} ')
    if not uri:
        raise Exception('require var uri: {uri} ')
    if not if_exists:
        raise Exception('require var if_exists:{if_exists} ')

    client = bigquery.Client()
    if service_account:
        client = bigquery.Client.from_service_account_json(service_account)

    table_id = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig()

    if file_format == "parquet":
        job_config.source_format = bigquery.SourceFormat.PARQUET
    elif file_format == "avro":
        job_config.source_format = bigquery.SourceFormat.AVRO
    elif file_format == "orc":
        job_config.source_format = bigquery.SourceFormat.ORC
    elif file_format == "json":
        job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    elif file_format == "csv":
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.skip_leading_rows = skip_leading_rows
        job_config.field_delimiter = delimiter
        job_config.quote_character = quotechar
        if encoding:
            job_config.encoding = encoding

    if schema:
        job_config.schema = schema
    else:
        job_config.autodetect = True

    if if_exists == "truncate":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    elif if_exists == "append":
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    try:
        load_job = client.load_table_from_uri(
            uri, table_id, job_config=job_config
        )
        load_job.result()
        logging.info(f"load Table {table_id} from uri gs://")
    except Conflict:
        logging.info(f"Provided Schema does not match Table {table_id} from uri gs://")
