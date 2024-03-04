from datetime import datetime
from time import sleep

import pytest
import zmail

from ingestation.modules.misc.utils import Notify
from ingestation.modules.outputs.loggers import Loggers
from ingestation_test.utils import generate_string


class TestNotify:
    """Class to test functions of Notify class"""

    content = generate_string(10)

    @staticmethod
    def find_content_in_last_mail(mail, auth, content) -> bool:
        server = zmail.server(mail, auth)
        latest = server.get_latest()

        # For NetEase mailbox, the content text can be in different places,
        # which depends on the mail format(html/text).
        # This may be updated after we test in other mailbox
        content_text = latest['content_text']
        if len(content_text) == 0:
            mail_content = str(latest['attachments'][0][-1])
        else:
            mail_content = latest['content_text'][0]

        if str.find(mail_content, content) == -1:
            return False
        return True

    @pytest.mark.parametrize("smtp, content, address", [
        [
            {
                "server": "smtp.163.com",
                "user": "13255193362@163.com",
                "password": "SVSVFEOTDIQQXHZC"
            },
            content, '13255193362@163.com']
    ])
    def test_send_mail(self, smtp, content, address):
        loggers = Loggers({})
        notify = Notify(list(address), loggers)

        notify.send_mail(smtp, content, address, datetime.now().strftime("%Y-%m-%d"))
        sleep(10)
        assert self.find_content_in_last_mail(smtp["user"], smtp["password"], content)
