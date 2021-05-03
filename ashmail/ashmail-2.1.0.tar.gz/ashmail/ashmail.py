from yaml import safe_load
from csv import reader
from jinja2 import Template
from argparse import ArgumentParser
from threading import Thread
from sys import exit

from ashmail.send import Send

from smtplib import SMTPAuthenticationError, SMTPDataError, SMTPServerDisconnected

class AshMail:
    def __init__(self, configuration: dict, content: str, recieversFile: str) -> None:
        with open(content) as content:
            content = content.read()
            self.template = Template(content)
        self.configuration = configuration
        self.recieversFile = recieversFile
        self.recievers = self.retrieveRecievers()

    def retrieveRecievers(self) -> dict:
        recievers = {}
        with open(self.recieversFile) as recieversFile:
            parsedRecieversFile = reader(recieversFile)
            for row in list(parsedRecieversFile)[1:]:
                name, email = row
                recievers[name] = email
        return recievers
    
    def parseSubject(self, subject: str, name: str, email: str) -> None:
        template = Template(subject)
        parsedSubject = template.render(name = name, subject = subject)
        self.configuration["subject"] = parsedSubject

    def run(self, name: str, email: str) -> None:
        content = self.template.render(name = name, email = email)
        self.parseSubject(
            self.configuration["subject"],
            name,
            email
        )
        send = Send(
            self.configuration["from"],
            self.configuration["password"],
            email,
            self.configuration["subject"],
            content
        )
        send.send()
        print(f"[INFO] Successfully sent email to {name} ({email})")

def retrieveConfigurationFile() -> str:
    argumentParser = ArgumentParser(
        prog = "ashmail",
        description = "the free and simple mass emailing system"
    )
    argumentParser.add_argument("configuration", help = "the name of the configuration file")
    arguments = argumentParser.parse_args()
    return arguments.configuration

def main() -> None:
    try:
        configuration = retrieveConfigurationFile()
        with open(configuration) as configuration:
            configuration = safe_load(configuration)
        print("AshMail - The Free and Simple Mass Emailing System")
        content = configuration["content"]
        recievers = configuration["recievers"]
        ashmail = AshMail(configuration, content, recievers)
        print("[INFO] Initializing Threads")
        for name in ashmail.recievers:
            email = ashmail.recievers[name]
            email = email.replace(" ", "")
            thread = Thread(target = ashmail.run, args = (name, email))
            thread.start()
    except FileNotFoundError:
        print("[ERROR] File Not Found")
        print(" Check the command-line arguments and configuration file for spelling errors.")
    except SMTPAuthenticationError:
        print("[ERROR] Gmail credentials not accepted by servers.")
        print(" This may be caused if you are not using an App Password or if Less-Secure Apps is disabled.")
    except (SMTPDataError, SMTPServerDisconnected):
        print("[ERROR] Gmail servers blocked message due to too many attempts for spam prevention.")
        print(" Please try again later.")
    except KeyboardInterrupt:
        print("[ERROR] Keyboard Interrupt")
        exit(1)
    except Exception as exception:
        print(f"[ERROR] An error occured: \"{str(exception)}\"")
        print(" Please open an issue at https://github.com/ashmail/ashmail to alert the developers.")
        print(" Include all the files and state any modifications to the code made.")