from datetime import timedelta

import yaml

from pydantic import BaseSettings


class ClassifierConfig(BaseSettings):
    """
    Конфигурация для клиента к модели классификатору.
    """
    # адрес сервиса
    host: str
    # порт сервиса
    port: int
    # таймаут на выполнение запроса, в секундах
    request_timeout: int


class AppConfig(BaseSettings):
    """
    Конфигурация приложения.
    """
    # Каталог для сохранения изображений
    images_dir: str
    # Конфигурация для клиента к модели классификатору
    classifier: ClassifierConfig
    # Через какой промежуток времени возможна следующая отправка изображения
    photo_rate_limit: timedelta


def read_config(
    config_path: str
) -> AppConfig:
    """
    По переданному пути прочитать содержимое yaml файла и сформировать
    конфигурация приложения на основе него.

    :param config_path:
        `str`, путь до файла с настройками.

    :return:
        `AppConfig`, конфигурация приложения.
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return AppConfig(**config)
