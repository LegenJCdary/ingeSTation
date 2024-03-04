from datetime import datetime
from os import getlogin, getuid, path
from pwd import getpwnam, getpwuid
from smtplib import SMTP, SMTPException
from socket import gethostname
from typing import Tuple

from ingestation.modules.outputs.loggers import Loggers


class InitParams:
    """
    Collection of basic parameters describing environment of Operator's upload process.
    """

    def __init__(self):
        self.start_point = self.get_start_point()
        self.caller_uid, self.caller_gid, self.caller_name = self.get_caller_id()
        self.hostname = gethostname()

    @staticmethod
    def get_start_point() -> datetime:
        return datetime.now()

    @staticmethod
    def get_caller_id() -> Tuple[int, int, str]:
        try:
            user = getpwnam(getlogin())
        # Detected on Ubuntu 20.04 LTS (GNU/Linux 5.10.16.3-microsoft-standard-WSL2 x86_64)
        except (FileNotFoundError, OSError):
            user = getpwuid(getuid())
        return user.pw_uid, user.pw_gid, user.pw_name


class Notify:

    def __init__(self, recipients: list, loggers: Loggers):
        self.recipients = recipients
        self.logger = loggers.logger

    @staticmethod
    def get_mail_content(content: str) -> str:
        if content is str and path.isfile(content):
            with open(content, "r", encoding="utf-8") as f:
                mail_content = f.readlines()
        else:
            mail_content = content

        return mail_content

    def send_notifications(self, smtp: dict, content: str):
        for address in self.recipients:
            self.send_mail(smtp, content, address, InitParams.get_start_point().strftime("%Y-%m-%d"))

    def send_mail(self, smtp: dict, content: str, address: str, date: str):
        smtp_server = smtp.get("server")
        smtp_username = smtp.get("user")
        smtp_password = smtp.get("password")

        mail_content = Notify.get_mail_content(content)
        with_subject = f"Subject: {' '.join([InitParams().hostname, date])}\n\n{mail_content}"

        try:
            with SMTP(smtp_server) as server:
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, address, with_subject)
        except SMTPException as exc:
            self.logger.error(f"Unable to send an e-mail due to '{exc}'.")
