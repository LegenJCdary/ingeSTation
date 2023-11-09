from logging import Logger
from json import loads
from typing import Union
import os

from jsonschema import validate

from .schemas import application, project, operator
from ..global_vars import global_vars
from .templates import templates


class Conf:
    """Class for parsing configuration files"""

    def __init__(self, conf_path: Union[bool, str], conf_type: str):
        self.conf_type = conf_type
        self.conf_path = self.get_conf_path(conf_path)

    def parse_conf(self) -> Union[bool, dict]:
        conf = self.load_conf()
        if self.validate_conf(conf) is None:
            return conf
        return False

    def validate_conf(self, conf: dict) -> None:
        if self.conf_type == "application":
            schema_file = application
        elif self.conf_type == "project":
            schema_file = project
        else:
            schema_file = operator
        return validate(instance=conf, schema=getattr(schema_file, self.conf_type))

    def load_conf(self) -> dict:
        with open(self.conf_path, "r", encoding="utf-8") as fh:
            return loads(fh.read())

    def get_conf_path(self, conf_path: Union[bool, str]) -> str:
        if not conf_path:
            conf_path = self.get_conf_here()
            if os.path.isfile(conf_path):
                return conf_path
            conf_path = os.path.join(global_vars.APPLICATION_DIR, f"{self.conf_type}.json")
            if os.path.isfile(conf_path):
                return conf_path
            raise FileNotFoundError(f"[CRITICAL]: {self.conf_type.capitalize()}"
                                    " configuration could not be obtained.")
        return conf_path

    def get_conf_here(self) -> str:
        for file in os.listdir(os.getcwd()):
            if file.endswith(f"{self.conf_type}.json"):
                return os.path.join(os.getcwd(), file)

        return ""


class ApplicationConf(Conf):
    """Class for application configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "application")
