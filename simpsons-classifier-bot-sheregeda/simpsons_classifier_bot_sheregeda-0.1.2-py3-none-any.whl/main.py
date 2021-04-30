import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pydantic import BaseModel

from simpsons_classifier_bot.classifier import ClassifierClient
from simpsons_classifier_bot.config import (
    read_config, AppConfig, ClassifierConfig
)
from simpsons_classifier_bot.handlers import start, photo, unknown


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


class Deps(BaseModel):
    """
    Инкапсулирует общие ресурсы приложения.
    """
    # клиент к классификатору Симпсонов
    classifier: ClassifierClient
    # конфигурация приложения
    config: AppConfig

    class Config:
        arbitrary_types_allowed = True


def make_classifier(
    config: ClassifierConfig
) -> ClassifierClient:
    """
    Создает и возвращает клиент к сервису модели классификатору.

    :param config:
        `ClassifierConfig`, Конфигурация для клиента.

    :return:
        `ClassifierClient`, экземпляр клиента.
    """
    return ClassifierClient(
        host=config.host, port=config.port,
        request_timeout=config.request_timeout
    )


def make_updater(
    token: str,
    deps: Deps,
) -> Updater:
    """
    Создает и возвращает обработчики сообщений для telegram бота.

    :param token:
        `str`, токен доступа к telegram.
    :param deps:
        `Deps`, общие ресурсы приложения.

    :return:
        `Updater`, класс "получатель" новых сообщений от telegram.
    """
    updater = Updater(token=token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.photo, photo, run_async=True)
    )
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text | Filters.command, unknown)
    )
    # FIXME: найти штатный способ добавления общих ресурсов в контекст хэндлера
    updater.dispatcher.deps = deps
    return updater


def run_app() -> None:
    """
    Запускает опрос и обработку новых сообщений от telegram бота.
    """
    config_dir = os.getenv('CONFIG_DIR')
    if config_dir is None:
        raise Exception('CONFIG_DIR env var is not specified')

    token = os.getenv('BOT_ACCESS_TOKEN')
    if token is None:
        raise Exception('BOT_ACCESS_TOKEN env var is not specified')

    config = read_config(config_path=os.path.join(config_dir, 'bot.yaml'))
    classifier = make_classifier(config=config.classifier)

    updater = make_updater(
        token=token, deps=Deps(classifier=classifier, config=config)
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_app()
