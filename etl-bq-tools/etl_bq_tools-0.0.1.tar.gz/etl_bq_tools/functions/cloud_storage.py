from google.cloud import storage


def gs_bucket_list(project_id, bucket_name, logging=None, key_path=None):
    """
    :param project_id: String
    :param bucket_name: String
    :param logging: Object
    :param key_path: file.json
    :return: list_blobs
    """
    if not project_id:
        raise Exception('require var project_id:{project_id} ')
    if not bucket_name:
        raise Exception('require var bucket_name:{bucket_name} ')

    client = storage.Client(project=project_id)
    if project_id and key_path:
        client = storage.Client.from_service_account_json(key_path)

    try:
        bucket = client.get_bucket(bucket_name)
        blobs = bucket.list_blobs()
        logging.info(f"list_blobs from  bucket {bucket_name} ")
        return blobs
    except Exception as e:
        logging.info(f"BucketName Not Found {bucket_name}")
