import os
import uuid
import functools

from datetime import datetime

from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from simpsons_classifier_bot.classifier import ClassifierError


def photo_rate_limit(func):
    """
    Декоратор, который не позволяет для одного и того же пользователя вызывать
    хэндлер по обработке изображения чаще, чем это указано в настройке
    `photo_rate_limit`.

    Отправляет сообщение в чат, если обнаружено превышение.
    """
    users = {}

    @functools.wraps(func)
    def wrapper(
        update: Update,
        context: CallbackContext,
    ):
        username = update.message.from_user.username
        limit = context.dispatcher.deps.config.photo_rate_limit
        now = datetime.now()

        if username in users:
            if now - users[username] < limit:
                context.dispatcher.logger.warning(
                    f'Rate limit for processing photo is exceeded, '
                    f'user: {username}'
                )
                update.message.reply_text(
                    f'Обработка изображения возможна не чаще, чем один раз '
                    f'в {limit.total_seconds()} секунд.',
                    reply_to_message_id=update.message.message_id
                )
                return

        users[username] = now
        return func(update, context)
    return wrapper


def start(
    update: Update,
    context: CallbackContext,
) -> None:
    """
    Хэндлер для команды 'start'. Отправляет приветственное сообщение.
    """
    context.dispatcher.logger.info(f'Handler "start": {update}')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Отправь мне изображение с персонажем из Симпсонов.'
    )


@photo_rate_limit
def photo(
    update: Update,
    context: CallbackContext,
) -> None:
    """
    Хэндлер для обработки отправленного изображения.

    Сохраняет картинку в каталог пользователя. Если каталог не существует, то
    создает его. После получения предсказания картинка удаляется.

    В ответ на переданную картинку с помощью модели классификатора вычисляет
    какой из персонажей Симпсонов изображен на ней и имя персонажа отправляется
    в чат.
    """
    context.dispatcher.logger.info(f'Handler "photo": {update}')
    username = update.message.from_user.username
    deps = context.dispatcher.deps

    os.makedirs(os.path.join(deps.config.images_dir, username), exist_ok=True)

    image_id = os.path.join(username, f'{str(uuid.uuid4())}.jpg')
    image_path = os.path.join(deps.config.images_dir, image_id)

    image = update.message.photo[-1].get_file()
    image.download(image_path)

    try:
        label = deps.classifier.predict(image_id=image_id)
    except ClassifierError:
        update.message.reply_text(
            'Произошла ошибка. Повторите запрос.',
            reply_to_message_id=update.message.message_id
        )
    else:
        update.message.reply_text(
            label, reply_to_message_id=update.message.message_id
        )

    os.remove(image_path)


def unknown(
    update: Update,
    context: CallbackContext,
) -> None:
    """
    Хэндлер для ответа на неподдерживаемый тип сообщений для бота.
    """
    context.dispatcher.logger.info(f'Handler "unknown": {update}')
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Я умею работать только с изображением.'
    )
