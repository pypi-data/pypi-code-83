# Copyright (c) 2019-2021 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

import os,sys,re
import re
import warnings
from pprint import pprint
import googleapps
import mimetypes

import email.encoders
import email.mime.text
import email.mime.multipart
from email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart

from bs4 import BeautifulSoup
import base64

import time
import datetime
import googleapiclient
import io

class GMail(googleapps.ServiceClient):
    default_api = 'gmail.send'
    default_api_version = 'v1'

    def __init__(self, gmail_user):
        super().__init__()
        self.gmail_user = gmail_user


    def send_message(self, message=None, *args, **kwargs):
        req = self._build_send_request(*args, **kwargs)
        return(self.make_request(req))


    def add_message(self, *args, **kwargs):
        req = self._build_send_request(*args, **kwargs)
        return(self.add_request(req))


    def _build_send_request(self, message=None, *args, callback=None, **kwargs):
        if not message:
            message = self.create_message(*args, **kwargs)
        else:
            if len(args) or len(kwargs):
                raise Exception("Invalid arguments : " + str(args) + " | " + str(kwargs))

        request = ServiceRequest(resource=['users', 'messages'],
                         function='send',
                         callback=callback,
                         parameters={'userId': self.gmail_user, 'body': message})
        return(request)


    def create_message(self, to, subject, message, reply_to=None, sender=None, cc=None, bcc=None, markdown=False, html=None, text_message=None, attachments=None):
        """
            message {str}: A general message, which is processed as follows:
                If markdown is true, it is assumed to be a markdown (or markdown-html hybrid message) and it is converted to html
                If html is not None, it indicates whether message is already in html or in text.
                If html is None, message will be conservatively searched for a set of html-tag looking things, which will make the determination
        """

        msg = email.mime.multipart.MIMEMultipart()
        msg['Subject'] = subject

        if markdown:
            message = self.markdown_to_html(message)
        else:
            if html is None:
                # -- search for common tags
                if re.search(r'\<\s*(br|p|i|b|li|ul|ol|strong)\s*\/?\s*\>', message, re.I):
                    html = True
                else:
                    html = False

            if not html:
                text_message = message
                message = self.htmlify_text(message)

        if not text_message:
            text_message = self.textify_html(message)

        #print("---- message ----", message)
        #print("\n\n\n---- text message ----", text_message)
        msg.attach(email.mime.text.MIMEText(message, 'html'))
        #msg.attach(email.mime.text.MIMEText(text_message, 'plain'))

        if attachments:
            if type(attachments) not in (list, tuple):
                attachments = [ attachments ]
            for attachment in attachments:
                attachpayload = self.prepare_attachment(attachment)
                msg.attach(attachpayload)

        if sender:
            msg['From'] = sender
        if to:
            if type(to) in (list, tuple):
                msg['To'] = ','.join(to)
            else:
                msg['To'] = to

        if cc:
            if type(cc) in (list, tuple):
                msg['CC'] = ','.join(cc)
            else:
                msg['CC'] = cc

        if bcc:
            if type(bcc) in (list, tuple):
                msg['BCC'] = ','.join(bcc)
            else:
                msg['BCC'] = bcc

        if reply_to:
            if type(reply_to) in (list, tuple):
                msg['Reply-To'] = ','.join(reply_to)
            else:
                msg['Reply-To'] = reply_to

        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}
        return(body)
        #return(email.encoders.encode_base64(msg))


    @classmethod
    def prepare_message(self, message, markdown=False, html=None, text_message=None):
        """
            message {str}: A general message, which is processed as follows:
                If markdown is true, it is assumed to be a markdown (or markdown-html hybrid message) and it is converted to html
                If html is not None, it indicates whether message is already in html or in text.
                If html is None, message will be conservatively searched for a set of html-tag looking things, which will make the determination
        """
        if markdown:
            message = self.markdown_to_html(message)
        else:
            if html is None:
                # -- search for common tags
                if re.search(r'\<\s*(br|p|i|b|li|ul|ol|strong)\s*\/?\s*\>', message, re.I):
                    html = True
                else:
                    html = False

            if not html:
                text_message = message
                message = self.htmlify_text(message)

        return(message)

    def prepare_attachment(self, filepath):

        my_mimetype, encoding = mimetypes.guess_type(filepath)

        # If the extension is not recognized it will return: (None, None)
        # If it's an .mp3, it will return: (audio/mp3, None) (None is for the encoding)
        #for unrecognized extension it set my_mimetypes to  'application/octet-stream' (so it won't return None again).
        if my_mimetype is None or encoding is not None:
            my_mimetype = 'application/octet-stream'


        main_type, sub_type = my_mimetype.split('/', 1)# split only at the first '/'
        # if my_mimetype is audio/mp3: main_type=audio sub_type=mp3

        #-----3.2  creating the attachement
            #you don't really "attach" the file but you attach a variable that contains the "binary content" of the file you want to attach

            #option 1: use MIMEBase for all my_mimetype (cf below)  - this is the easiest one to understand
            #option 2: use the specific MIME (ex for .mp3 = MIMEAudio)   - it's a shorcut version of MIMEBase

        #this part is used to tell how the file should be read and stored (r, or rb, etc.)
        if main_type == 'text':
            print("text")
            temp = open(filepath, 'r')  # 'rb' will send this error: 'bytes' object has no attribute 'encode'
            attachment = MIMEText(temp.read(), _subtype=sub_type)
            temp.close()

        elif main_type == 'image':
            print("image")
            temp = open(filepath, 'rb')
            attachment = email.mime.image.MIMEImage(temp.read(), _subtype=sub_type)
            temp.close()

        elif main_type == 'audio':
            print("audio")
            temp = open(filepath, 'rb')
            attachment = email.mime.audio.MIMEAudio(temp.read(), _subtype=sub_type)
            temp.close()

        elif main_type == 'application' and sub_type == 'pdf':
            from email.mime.application import MIMEApplication
            temp = open(filepath, 'rb')
            attachment = MIMEApplication(temp.read(), _subtype=sub_type)
            temp.close()

        else:
            attachment = email.mime.base.MIMEBase(main_type, sub_type)
            temp = open(filepath, 'rb')
            attachment.set_payload(temp.read())
            temp.close()

        #-----3.3 encode the attachment, add a header and attach it to the message
        email.encoders.encode_base64(attachment)  #https://docs.python.org/3/library/email-examples.html
        filename = os.path.basename(filepath)
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        return(attachment)

    def prepare_attachment_GOOGLE(self, attachment):
          """ stolen from the google developer api """

          content_type, encoding = mimetypes.guess_type(attachment)

          if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
          main_type, sub_type = content_type.split('/', 1)
          if main_type == 'text':
            fp = open(attachment, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
          elif main_type == 'image':
            fp = open(attachment, 'rb')
            msg = email.mime.image.MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
          elif main_type == 'audio':
            fp = open(attachment, 'rb')
            msg = email.mime.audio.MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
          else:
            fp = open(attachment, 'rb')
            msg = email.mime.base.MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
          filename = os.path.basename(attachment)
          return(filename, msg)

    @classmethod
    def textify_html(cls, html):
        text_message = html
        # invert links
        text_message = re.sub(r'<a[^>]+href\s*=\s*[\'"]\s*([^"\']+?)\s*[\'"].*?>(.*?)<\s*/a\s*>',
                              lambda x: x.group(2) + " (" + x.group(1) + ")  ",
                              text_message)
        # now paragraphs
        text_message = re.sub(r'<p>', "\n\n", text_message)

        #de-tag
        soup = BeautifulSoup(text_message, 'lxml')
        text_message = soup.get_text()
        return(text_message)

    @classmethod
    def htmlify_text(cls, text):
        # change linebreaks
        html_message = text
        html_message = re.sub(r"\n", '<br />', html_message)
        return(html_message)

    @classmethod
    def markdown_to_html(cls, msg, pretty=True):
        result_message = []
        in_list = False
        lines = msg.split("\n")
        htmlre = re.compile('(https?:\/\/[^\s]+)', re.I)
        for iline, line in enumerate(lines):

            # handle markdown links: [text label](http://href)
            line = re.sub(r'\[([^\]\r\n]+)\]\s*\(((http|ftp|mailto)[^\)\r\n]+)\)', lambda m: '<a href="'+m.group(2)+'">' + m.group(1) + '</a>', line)

            # handle header formatting
            m = re.match(r'(#+)\s+(.*)', line)
            if m:
                head_level =str(len(m.group(1)))
                line = '<h' + head_level  + '>' + m.group(2) + '</h' + head_level + '>'

            # before we do these, let's sub out html urls because wonky things happen
            presubs = {}
            presub_iter = 1
            mhtml = htmlre.search(line)
            while mhtml:
                repl = f'@@temp:{presub_iter}@@'
                line = line.replace(mhtml.group(1), repl)
                presubs[repl] = mhtml.group(1)
                presub_iter += 1
                mhtml = htmlre.search(line)

            # italics and bold
            line = re.sub(r'\*\*([^\*]+)\*\*', lambda m: '<b>' + m.group(1) + '</b>', line)
            line = re.sub(r'\_\_([^\_<>]+)\_\_', lambda m: '<b>' + m.group(1) + '</b>', line)
            #line = re.sub(r'\_([^\_<>]+)\_', lambda m: '<i>' + m.group(1) + '</i>', line)
            line = re.sub(r'\*([^\*]+)\*', lambda m: '<i>' + m.group(1) + '</i>', line)

            #
            # Now we can replace everythig in the line
            #
            for key, value in presubs.items():
                line = line.replace(key, value)

            # handle lists
            if re.match(r'\d+\.\s+', line):
                m = re.match(r'\d+\.\s+(.*)', line)
                if not in_list:
                    result_message.append('<ol>')
                    in_list = 'ol'
                result_message.append('<li>' + m.group(1) + '</li>')
            elif re.match(r'[\*\-\+]\s+', line):
                m = re.match(r'[\*\-\+]\s+(.*)', line)
                if not in_list:
                    result_message.append('<ul>')
                    in_list = 'ul'
                result_message.append('<li>' + m.group(1) + '</li>')
            elif re.match(r'\s*$', line):
            # This is a blank line.
            # if there is a blank line that is at the end of a list block, we just end the list
            # if there is a blank line that is not in a list context, we consider it an actual request for linebreak
                if in_list:
                    # any break ends the list
                    result_message.append('</'+in_list+'>')
                    in_list = False
                else:
                    result_message.append('<br />')
            elif iline == len(lines) - 1:
                # this is the last line of lines, so just add the text.
                result_message.append(line)
            else:
                # Not the last line!  So add the text and then a line break
                result_message.append(line + '<br />')

        # clean up any open tags
        if in_list:
            result_message.append('</'+in_list+'>')

        return(''.join(result_message))
