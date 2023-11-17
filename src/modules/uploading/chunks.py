import os


class Crate:

    def __init__(self):
        pass

    def create_crate(self):
        try:
            os.mkdir()
        except Exception as exc:
            raise exc