from etl_bq_tools.utils.time_execution import get_time_function_execution


def bq_set_project(project_id=None, logging=None):
    """
    :param project_id: String
    :param logging: Object
    :return:
    """
    import os

    if not project_id:
        raise Exception('require var project_id: {project_id} ')
    try:
        os.system(f"gcloud config set project {project_id}")
        logging.info(f"project update {project_id} ")
    except:
        logging.info(f"Project Not Found: {project_id} ")


@get_time_function_execution
def bq_execute_sql(sql=None, parameter=None, logging=None):
    """
    :param sql: file.sql
    :param parameter: {"parameter:[{"variable": "", "type": "", "value":""}]}
    :param logging: object
    :return:
    """

    import os

    if not sql:
        raise Exception('require var sql: {file.sql} ')

    file_sql = os.path.basename(sql)

    try:
        _parameter = ""
        if parameter:
            for key, values in parameter.items():
                for value in values:
                    _var = value["variable"]
                    _type = value["type"]
                    _val = value["value"]
                    _parameter = f"--parameter={_var}:{_type}:{_val}"
                    _parameter += f" {_parameter} \\ "

            sentence_bq = f"bq query --quiet  --use_legacy_sql=false {_parameter} --flagfile={sql} "
        else:
            sentence_bq = f"bq query --quiet  --use_legacy_sql=false --flagfile={sql} "
        os.system(sentence_bq)
        logging.info(f"Successfully: {file_sql}")
    except Exception as e:
        logging.info(f"Error: {file_sql}")
