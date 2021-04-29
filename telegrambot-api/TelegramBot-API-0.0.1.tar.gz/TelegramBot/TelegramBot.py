from requests import post


class TelegramBot:
    """
    With this class you can send any data in 'str' format\n
    to your telegram account through an already created \n
    telegram bot.
    """
    def __init__(self, bot_token: str):
        self.__bot_token = bot_token
        self.httpdebugger_url = "https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx"
        self.telegram_api_url = f"https://api.telegram.org/bot{self.__bot_token}/"
        
    def sendMessage(self, chat_id, text: str):
        """
        Use this method to send a plain text;
        Simply just give your plain text to it.
        """
        url = self.telegram_api_url + f"SendMessage?chat_id={chat_id}&text={text}"
        data_dict = {
            "UrlBox": url,
            "AgentList": "Mozilla Firefox",
            "VersionsList": "HTTP/1.1",
            "MethodList": "POST"
        }
        req = post(self.httpdebugger_url, data=data_dict)

        return req

    def sendPhoto(self, chat_id, photo,
                  caption: str = None,
                  parse_mode: str = None,
                  disable_notification: bool = None):
        """
        Uploads a photo from your local machine
        to your telegram account.
        """
        # Real telegram api to upload photos using a telegram bot.
        url = self.telegram_api_url + "sendPhoto"
        photo_file = {
            'photo': open(photo, 'rb')
        }
        data = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_notification": disable_notification
        }
        req = post(url, files=photo_file, data=data)
        return req

    def sendDocument(self, chat_id, document,
                     caption: str = None,
                     parse_mode: str = None,
                     disable_content_type_detection: bool = None,
                     disable_notification: bool = None):
        """
        Uploads a general file or document (text file, photo, etc.)
        from your local machine to your telegram account.
        """
        url = self.telegram_api_url + "sendDocument"
        document_file = {
            "document": open(document, "rb")
        }
        data = {
            "chat_id": chat_id,
            "caption": caption,
            "parse_mode": parse_mode,
            "disable_content_type_detection": disable_content_type_detection,
            "disable_notification": disable_notification
        }
        req = post(url, files=document_file, data=data)
        return req
