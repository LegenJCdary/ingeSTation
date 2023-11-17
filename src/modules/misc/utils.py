from datetime import datetime
from os import getlogin
from pwd import getpwnam
from socket import gethostname
from typing import Tuple


class InitParams:

    def __init__(self):
        self.start_point = self.get_start_point()
        self.caller_uid, self.caller_gid, self.caller_name = self.get_caller_id()
        self.hostname = gethostname()

    @staticmethod
    def get_start_point() -> str:
        return datetime.now()

    @staticmethod
    def get_caller_id() -> Tuple[int, int, str]:
        user = getpwnam(getlogin())
        return user.pw_uid, user.pw_gid, user.pw_name


class Notify:

    def __init__(self, recipients: list):
        self.recipients = recipients

    def send_notifications(self):
        for name, address in self.recipients:
            self.send_notification(name, address)

    def send_notification(self, name, address):
        if "@" in address:
            self.send_email(name, address)

    @staticmethod
    def send_mail(content: str, recipients: list, date: str, logger: logging):
        if content is str and os.path.isfile(content):
            mail_content = open(content, "r").readlines()
        else:
            mail_content = content
        with_subject = 'Subject: {}\n\n{}'.format(" ".join([gethostname(), date]), mail_content)

        try:
            with smtplib.SMTP("localhost") as server:
                server.sendmail("upload_script", recipients, with_subject)
        except Exception as exc:
            logger.error('Unable to send an e-mail due to "{}".'.format(exc))
