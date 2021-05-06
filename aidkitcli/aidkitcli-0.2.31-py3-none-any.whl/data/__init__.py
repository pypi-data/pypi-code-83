"""To upload a new data set to aidkit, you can upload either a zip file or
directly a pandas DataFrame.

In both cases, you only need to upload a data set once and then you'll be able
to reuse it for future quality analyses (:ref:`example-upload-data-set`).
"""
from aidkitcli.data_access.upload import upload_data, list_data
