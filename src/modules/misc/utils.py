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
