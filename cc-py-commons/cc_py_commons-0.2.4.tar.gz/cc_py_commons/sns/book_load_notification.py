import json

from cc_py_commons.sns.sns_service import SnsService

class BookLoadNotification:

  def __init__(self, app_config):
    self._app_config = app_config

  def send(self, load_id, user_id):
    message = '{' + f'"userId" : {user_id}, ' \
                    f'"load_id": "{load_id}", ' \
                    f'"subject" : "{self._app_config.BOOK_LOAD_SNS_SUBJECT}", ' \
                    f'"className":  "{self._app_config.BOOK_LOAD_SNS_CLASS_NAME}"' + '}'
    sns_service = SnsService()
    sns_service.send(self._app_config.BOOK_LOAD_SNS_TOPIC_ARN,
      self._app_config.BOOK_LOAD_SNS_SUBJECT, message)
