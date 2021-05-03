from storage import StorageItem, StorageSearchIter, Storage
import boto3
import os

class S3StorageItem(StorageItem):
    Key = None
    name = None
    LastModified = None
    ETag = None
    Size = None
    StorageClass = None
    Owner = None

    def __init__(self, data: dict):
        self.Key = data['Key'] if 'Key' in data else None
        self.LastModified = data['LastModified'] if 'LastModified' in data else None
        self.ETag = data['ETag'] if 'ETag' in data else None
        self.Size = data['Size'] if 'Size' in data else None
        self.StorageClass = data['StorageClass'] if 'StorageClass' in data else None
        self.Owner = data['Owner'] if 'Owner' in data else None
        if not self.Key:
            raise ValueError("Must specify a key")
        self.name = self.Key.rsplit('/', 1)[-1]
        super().__init__()

    def __str__(self):
        return self.name


class S3StorageObjectIter(StorageSearchIter):
    def __init__(self, client: boto3.client = None, bucket: str = None, basepath: str = "", pagesize: int = 100):
        self._client = client
        self._bucket = bucket
        self._basepath = basepath
        self._pagesize = pagesize

        self.response = self._client.list_objects_v2(
            Bucket=self._bucket,
            EncodingType='url',
            MaxKeys=self._pagesize,
            Prefix=self._basepath
        )
        self.index = 0
        super().__init__()

    def __iter__(self):
        return self

    def _fetchNewS3Page(self):
        if not self.response['IsTruncated']:
            return False
        self.response = self._client.list_objects_v2(
            Bucket=self._bucket,
            EncodingType='url',
            MaxKeys=self._pagesize,
            Prefix=self._basepath,
            ContinuationToken=self.response['NextContinuationToken']
        )
        return True

    def __next__(self):
        index = self.index
        if index >= self._pagesize:
            if not self._fetchNewS3Page():
                raise StopIteration
            index = 0
        content = self.response['Contents']
        if index >= len(content):
            raise StopIteration
        ret = content[index]
        self.index = index + 1
        return S3StorageItem(ret)


class S3Storage(Storage):
    _client = None
    _bucket = None
    ItemTypes = [type(S3StorageItem)]

    def __init__(self, s3_client: boto3.client, bucket_name: str):
        self._client = s3_client
        self._bucket = bucket_name
        super().__init__()

    def search(self, basepath: str = "", pagesize: int = 100):
        return S3StorageObjectIter(self._client, self._bucket, basepath=basepath, pagesize=pagesize)

    def put(self, o: S3StorageItem, filepath: str):
        if not isinstance(o, S3StorageItem):
            raise ValueError(f"Provided object is of type {str(type(o))}, requires S3StorageObject")

        self._client.upload_file(
            filepath,
            self._bucket,
            o.Key
        )

        return True

    def get(self, o: StorageItem, filepath=""):
        if type(o) not in self.ItemTypes:
            raise ValueError(f"Provided object is of type {str(type(o))}, requires S3StorageObject")
        key = o.Key
        tmp = filepath.rsplit('/', 1)
        if filepath == "":
            filepath = tmp[1]
        if tmp != "":
            os.makedirs(tmp[0], exist_ok=True)
        self._client.download_file(self._bucket, key, filepath)
        return filepath

    def delete(self, o: StorageItem):
        if type(o) not in self.ItemTypes:
            raise ValueError(f"Provided object is of type {str(type(o))}, requires S3StorageObject")

        key = o.Key

        self._client.delete_object(
            Bucket=self._bucket,
            Key=key
        )

        return True

