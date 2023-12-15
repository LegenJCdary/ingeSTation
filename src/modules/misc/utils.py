from datetime import datetime
from os import getlogin, getuid
from pwd import getpwnam, getpwuid
from socket import gethostname
from typing import Tuple


class InitParams:

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
        except FileNotFoundError:
            user = getpwuid(getuid())
        return user.pw_uid, user.pw_gid, user.pw_name
