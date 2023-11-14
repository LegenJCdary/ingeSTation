import os
from json import loads
from typing import Union

from jsonschema import validate, ValidationError

from ingestation.modules.configs.schemas import application, project, operator
from ingestation.modules.global_vars import APPLICATION_DIR


def convert_schema_name(schema_file):
    module_name = str.split(str(schema_file), "'")[1]
    config_file_name = str.split(module_name, ".")[-1]

    return config_file_name


def validate_json(conf: dict, schema_file) -> None:
    try:
        validate(instance=conf, schema=getattr(schema_file, "schema"))
    except ValidationError as ex:
        raise ValidationError(
            f"[CRITICAL]: {convert_schema_name(schema_file).capitalize()} "
            f"config validation failed. {str(ex)}") \
            from ex


class Conf:
    """Class for parsing configuration files"""

    def __init__(self, conf_path: Union[bool, str], conf_type: str, schema_file):
        self.conf_type = conf_type
        self.conf_path = self.get_conf_path(conf_path)
        self.schema_file = schema_file

    def parse_conf(self) -> Union[bool, dict]:
        conf = self.load_conf()
        validate_json(conf, self.schema_file)

        return conf

    def load_conf(self) -> dict:
        with open(self.conf_path, "r", encoding="utf-8") as fh:
            return loads(fh.read())

    def get_conf_path(self, conf_path: Union[str, bool]) -> str:
        if not conf_path:
            conf_path = os.path.join(APPLICATION_DIR, f"{self.conf_type}.json")
            if os.path.isfile(conf_path):
                return conf_path
            raise FileNotFoundError(f"[CRITICAL]: {self.conf_type.capitalize()} "
                                    f"configuration could not be found at {APPLICATION_DIR}.")
        if os.path.isfile(conf_path):
            return conf_path

        raise FileNotFoundError(f"[CRITICAL]: {self.conf_type.capitalize()} "
                                f"configuration could not be found: {conf_path}.")


class ApplicationConf(Conf):
    """Class for application configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "application", application)


class ProjectConf(Conf):
    """Class for project configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "project", project)


class OperatorConf(Conf):
    """Class for operator configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "operator", operator)
