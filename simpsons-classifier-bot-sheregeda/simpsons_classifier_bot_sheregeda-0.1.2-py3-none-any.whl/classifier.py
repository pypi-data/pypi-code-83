import logging

import httpx


class ClassifierError(Exception):
    """
    Базовый класс для ошибок классификатора.
    """


class NotFound(ClassifierError):
    """
    Ресурс не найден.
    """


class ClassifierClient:
    """
    Класс для взаимодействия с сервисом классификатором Симпсонов.
    """
    logger = logging.getLogger('ClassifierClient')

    def __init__(self, host, port, request_timeout):
        self.client = httpx.Client(
            base_url=f'http://{host}:{port}/v1', timeout=request_timeout
        )

    def predict(
        self, image_id: str
    ) -> str:
        """
        Выполнить запрос на предсказание персонажа, который изображен на
        картинке с переданным идентификатором.

        :param image_id:
            `str`, идентификатор картинки.

        :return:
            `str`, наименование персонажа.

        :raise NotFound:
            Классификатор не нашел картинку с указанным идентификатором.
        :raise ClassifierError:
            При всех остальных ошибках классификатора.
        """
        body = {'image_id': image_id}

        try:
            response = self.client.post('/predict', json=body)
        except httpx.ReadTimeout:
            self.logger.error(
                f'Method: "predict", request: {body}, response: ReadTimeout'
            )
            raise ClassifierError

        status_code = response.status_code

        if status_code == httpx.codes.NOT_FOUND:
            self.logger.error(f'Image not found. Request: {body}')
            raise NotFound

        if status_code != httpx.codes.OK:
            self.logger.error(
                f'Unexpected response for "predict" method. Request: {body}, '
                f'code: {status_code}, response: {response}'
            )
            raise ClassifierError

        result = response.json()
        self.logger.info(
            f'Method: "predict", request: {body}, response: {result}'
        )
        return result['label']
