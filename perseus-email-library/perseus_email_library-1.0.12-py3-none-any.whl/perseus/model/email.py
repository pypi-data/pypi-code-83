# Copyright (C) 2019 Majormode.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from majormode.perseus.utils import string_util


class Mailbox:
    def __init__(self, email_address, name=None):
        """
        Build an object `Mailbox`.


        :param email_address: Electronic mail address of the mailbox.

        :param name: The name of the owner of this mailbox, generally the
            full name of a person.
        """
        if not string_util.is_email_address(email_address):
            raise ValueError(f'The email address "{email_address}" is not valid')

        self.__name = name and name.strip()
        self.__email_address = email_address.strip().lower()

    @property
    def email_address(self):
        return self.__email_address

    @staticmethod
    def from_json(payload):
        return payload and Mailbox(
            payload['email_address'],
            name=payload.get('name')
        )

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'"{self.__name}" <{self.__email_address}>'


class Email:
    """
    Represent a message to be sent as an electronic mail to recipient(s).
    """
    def __init__(
            self,
            author,
            recipients,
            subject,
            bcc_recipients=None,
            cc_recipients=None,
            html_content=None,
            text_content=None,
            attached_files=None,
            unsubscribe_mailto_link=None,
            unsubscribe_url=None):
        """
        Build an object `Email`.


        :param author: An `Mailbox` object representing the author, with the
            email address of the mailbox to which the author of the message
            suggests that replies be sent.

        :param recipients: An object or a collection of objects `Mailbox`
            representing the recipient(s) of the message.

        :param subject: A short string identifying the topic of the message.

        :param bcc_recipients: An object or a collection of objects `Mailbox`
            representing the Blind Carbon Copy (BCC) recipient(s) of the
            message.

            The other recipients of the message won’t be able to see that these
            BBC recipient have been sent a copy of the email.

        :param cc_recipients: An object or a collection of objects `Mailbox`
            representing the Carbon Copy (CC) recipient(s) of the message.

            Using CC is more a matter of etiquette than anything. The general
            rule is that the "To" field is reserved for the main recipients of
            an email. Other interested parties can be included as a CC so they
            can have their own copy of the email.

        :param html_content: The HTML body of the message.

        :param text_content: The plain text body of the message.

        :param attached_files: A string or a collection of strings
            corresponding to the full path and name of the files to attached
            to this message.

        :param unsubscribe_mailto_link: an email address to directly
            unsubscribe the recipient who requests to be removed from the
            mailing list (https://tools.ietf.org/html/rfc2369.html).

            In addition to the email address, other information can be provided.
            In fact, any standard mail header fields can be added to the mailto
            link.  The most commonly used of these are "subject", "cc", and "body"
            (which is not a true header field, but allows you to specify a short
            content message for the new email). Each field and its value is
            specified as a query term (https://tools.ietf.org/html/rfc6068).

        :param unsubscribe_url: a link that will take the subscriber to a
            landing page to process the unsubscribe request.  This can be a
            subscription center, or the subscriber is removed from the list
            right away and gets sent to a landing page that confirms the
            unsubscribe.
        """
        if not html_content and not text_content:
            raise ValueError("Empty content")

        self.__author = author
        self.__recipients = self.__build_list(recipients)
        self.__cc_recipients = self.__build_list(cc_recipients)
        self.__bcc_recipients = self.__build_list(bcc_recipients)
        self.__subject = subject
        self.__text_content = text_content
        self.__html_content = html_content
        self.__attached_files = attached_files
        self.__unsubscribe_mailto_link = unsubscribe_mailto_link
        self.__unsubscribe_url = unsubscribe_url

    @staticmethod
    def __build_list(element_or_list):
        return element_or_list and \
            (element_or_list if isinstance(element_or_list, (list, set, tuple)) else [element_or_list])

    @property
    def are_unsubscribe_methods_available(self):
        return self.__unsubscribe_mailto_link is not None or self.__unsubscribe_url is not None

    @property
    def attached_files(self):
        return self.__attached_files

    @property
    def author(self):
        """
        Return the author of the message.


        :return: An object `UserEmail` corresponding to the author of the
            message.
        """
        return self.__author

    @property
    def bcc_recipients(self):
        """
        Return the Blind Carbon Copy recipient(s) of the message.


        :return: An object or a collection of objects `Mailbox`.
        """
        return self.__bcc_recipients

    @property
    def cc_recipients(self):
        """
        Return the Carbon Copy recipient(s) of the message.


        :return: An object or a collection of objects `Mailbox`.
        """
        return self.__cc_recipients

    @property
    def content(self):
        """
        Return the body of the message, preferably the HTML content.


        :return: The body of the message.
        """
        return self.__html_content or self.__text_content

    @staticmethod
    def __parse_recipients_from_json(payload):
        if not payload:
            return None

        recipients = Mailbox.from_json(payload) if not isinstance(payload, list) \
            else [
                Mailbox.from_json(recipient_json)
                for recipient_json in payload
            ]

        return recipients

    @classmethod
    def from_json(cls, payload):
        if payload is None:
            return None

        author = Mailbox.from_json(payload['author'])
        subject = payload['subject']
        recipients = cls.__parse_recipients_from_json(payload['recipients'])
        cc_recipients = cls.__parse_recipients_from_json(payload.get('cc_recipients'))
        bcc_recipients = cls.__parse_recipients_from_json(payload.get('bcc_recipients'))
        html_content = payload.get('html_content')
        text_content = payload.get('text_content')

        return Email(
            author,
            recipients,
            subject,
            bcc_recipients=bcc_recipients,
            cc_recipients=cc_recipients,
            html_content=html_content,
            text_content=text_content
        )

    @property
    def html_content(self):
        """
        Return the HTML body of the message.


        :return: The HTML body of the message.
        """
        return self.__html_content

    @property
    def recipients(self):
        """
        Return the list of primary recipients of the message.


        :return: A collection of `Mailbox` objects.
        """
        return self.__recipients

    @property
    def subject(self):
        """
        Return the topic of the message.


        :return: A short string identifying the topic of the message.
        """
        return self.__subject

    @property
    def text_content(self):
        """
        Return the textual body of the message.


        :return: The textual body of the message.
        """
        return self.__text_content

    @property
    def unsubscribe_mailto_link(self):
        return self.__unsubscribe_mailto_link

    @property
    def unsubscribe_url(self):
        return self.__unsubscribe_url
