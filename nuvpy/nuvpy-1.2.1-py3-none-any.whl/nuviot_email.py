import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email

from sendgrid.helpers.mail.attachment import Attachment
import base64
from sendgrid.helpers.mail.file_content import FileContent
from sendgrid.helpers.mail.file_type import FileType
from sendgrid.helpers.mail.file_name import FileName
from sendgrid.helpers.mail.disposition import Disposition

reports_from_name = os.environ.get('Smtp__FromName')
reports_from_email = os.environ.get('Smtp__FromAddress')
sendgrid_api_key = os.environ.get('Smtp__Token')

def sendReport(to_emails, full_output_file, file_name, msg_subject, msg_content):
    message = Mail(
        from_email=Email(reports_from_email, reports_from_name),
        to_emails=to_emails,
        subject=msg_subject,
        html_content=msg_content)

    with open(full_output_file, 'rb') as f:
        data = f.read()
        f.close()

    encoded_file = base64.b64encode(data).decode()

    message.attachment = Attachment(FileContent(encoded_file), FileName(file_name), FileType('application/pdf'), Disposition('attachment'))

    sg = SendGridAPIClient(sendgrid_api_key)
    response = sg.send(message)
    if(response.status_code >= 200 and response.status_code < 300):
        print("success sending: " + full_output_file + " to " + to_emails + " ok")
    else:
        print("could not send email")
        print(response.status_code, response.body, response.headers)
