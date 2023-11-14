import os
from logging import Logger
from json import loads
from typing import Union
from jsonschema import validate

import schemas
from ..global_vars import APPLICATION_DIR, CONFIG_RULES, MANDATORY_KEYS, PRECEDENCE_RULES
from .templates import templates


class Conf:
    """Class for parsing configuration files"""

    def __init__(self, conf_path: Union[bool, str], conf_type: str, schema_file: schemas):
        self.conf_type = conf_type
        self.conf_path = self.get_conf_path(conf_path)
        self.schema_file = schema_file

    def parse_conf(self) -> Union[bool, dict]:
        conf = self.load_conf()
        if self.validate_conf(conf) is None:
            return conf
        return False

    def validate_conf(self, conf: dict) -> None:
        if self.conf_type == "application":
            schema_file = schemas.application
        elif self.conf_type == "project":
            schema_file = schemas.project
        else:
            schema_file = schemas.operator
        return validate(instance=conf, schema=getattr(schema_file, self.conf_type))

    def load_conf(self) -> dict:
        with open(self.conf_path, "r", encoding="utf-8") as fh:
            return loads(fh.read())

    def get_conf_path(self, conf_path: Union[bool, str]) -> str:
        if not conf_path:
            if os.path.isfile(conf_path):
                return conf_path
            conf_path = os.path.join(APPLICATION_DIR, f"{self.conf_type}.json")
            if os.path.isfile(conf_path):
                return conf_path
            raise FileNotFoundError(f"[CRITICAL]: {self.conf_type.capitalize()}"
                                    " configuration could not be obtained.")
        return conf_path
