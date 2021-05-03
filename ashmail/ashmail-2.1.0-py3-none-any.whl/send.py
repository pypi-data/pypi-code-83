from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Send:
    def __init__(
            self,
            fromEmail: str,
            fromEmailPassword: str,
            toEmail: str,
            subject: str,
            content: str
        ) -> None:
        self.fromEmail = fromEmail
        self.fromEmailPassword = fromEmailPassword
        self.toEmail = toEmail
        self.subject = subject
        self.content = content
        self.initializeMessage()
    
    def initializeMessage(self) -> None:
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = self.subject
        self.message["From"] = self.fromEmail
        self.message["To"] = self.toEmail
    
    def send(self) -> None:
        self.message.attach(
            MIMEText(self.content, "html")
        )
        smtpServer = SMTP("smtp.gmail.com", 587)
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.login(self.fromEmail, self.fromEmailPassword)
        smtpServer.sendmail(
            self.fromEmail,
            self.toEmail,
            self.message.as_string()
        )
        smtpServer.quit()
