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


class ApplicationConf(Conf):
    """Class for application configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "application", schemas.application)


class ProjectConf(Conf):
    """Class for project configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "project", schemas.project)


class OperatorConf(Conf):
    """Class for operator configuration files"""

    def __init__(self, conf_path: Union[str, bool]):
        super().__init__(conf_path, "operator", schemas.operator)


class MergedConf:
    """Class for merging configuration files"""

    def __init__(self, logger: Logger):
        self.logger = logger

        self.operator = OperatorConf(os.path.join(APPLICATION_DIR, "operator.json")).parse_conf()
        self.project = ProjectConf(os.path.join(APPLICATION_DIR, "project.json")).parse_conf()
        self.application = ApplicationConf(os.path.join(APPLICATION_DIR, "application.json")).parse_conf()

        self.operator_keys = self.flatten_dict(
            self.operator, exclude_keys=CONFIG_RULES["exclude_flatten"])
        self.project_keys = self.flatten_dict(
            self.project, exclude_keys=CONFIG_RULES["exclude_flatten"])
        self.application_keys = self.flatten_dict(
            self.application, exclude_keys=CONFIG_RULES["exclude_flatten"])

        self.final = self.create_final_conf()

    def flatten_dict(self, dct, parent_key="", sep="_", exclude_keys=None):
        if exclude_keys is None:
            exclude_keys = []
        flattened = {}
        for key, value in dct.items():
            if key in exclude_keys:
                flattened[key] = value
            else:
                new_key = f"{parent_key}{sep}{key}" if parent_key else key
                if isinstance(value, list):
                    for idx, item in enumerate(value):
                        item_key = f"{new_key}{sep}{idx}"
                        if isinstance(item, dict):
                            flattened.update(self.flatten_dict(item, item_key, sep))
                        else:
                            flattened[item_key] = item
                elif isinstance(value, dict):
                    flattened.update(self.flatten_dict(value, new_key, sep))
                else:
                    flattened[new_key] = value
        return flattened

    def create_final_conf(self) -> dict:
        final_conf = {}
        for key in templates.merged:
            if key in CONFIG_RULES["exclude_flatten"]:
                final_conf[key] = self.merge_conf(key)
            else:
                final_conf[key] = self.overwrite_conf(key)
            if not final_conf[key] and key in MANDATORY_KEYS:
                # pylint: disable=broad-exception-raised
                raise Exception(f"Missing mandatory value of: {key}")
        return final_conf

    def merge_conf(self, key: str):
        if key in CONFIG_RULES["merge_to_dict"]:
            merge_conf = {}
            if key in self.application_keys:
                merge_conf.update(self.application_keys[key])
            if key in self.project_keys:
                merge_conf.update(self.project_keys[key])
            if key in self.operator_keys:
                merge_conf.update(self.operator_keys[key])

            return merge_conf

        merge_conf = []
        if key in self.application_keys:
            merge_conf.extend(self.application_keys[key])
        if key in self.project_keys:
            merge_conf.extend(self.project_keys[key])
        if key in self.operator_keys:
            merge_conf.extend(self.operator_keys[key])

        return merge_conf

    def overwrite_conf(self, key: str):
        # pylint: disable=too-many-return-statements, too-many-branches
        if key in PRECEDENCE_RULES["app_proj_op"]:
            if key in self.application_keys:
                return self.application_keys[key]
            if key in self.project_keys:
                return self.project_keys[key]
            return self.operator_keys[key]
        if key in PRECEDENCE_RULES["app_op_proj"]:
            if key in self.application_keys:
                return self.application_keys[key]
            if key in self.operator_keys:
                return self.operator_keys[key]
            return self.project_keys[key]
        if key in PRECEDENCE_RULES["proj_op_app"]:
            if key in self.project_keys:
                return self.project_keys[key]
            if key in self.operator_keys:
                return self.operator_keys[key]
            return self.application_keys[key]
        if key in PRECEDENCE_RULES["proj_app_op"]:
            if key in self.project_keys:
                return self.project_keys[key]
            if key in self.application_keys:
                return self.application_keys[key]
            return self.operator_keys[key]
        if key in PRECEDENCE_RULES["op_app_proj"]:
            if key in self.operator_keys:
                return self.operator_keys[key]
            if key in self.application_keys:
                return self.application_keys[key]
            return self.project_keys[key]
        if key in self.operator_keys:
            return self.operator_keys[key]
        if key in self.project_keys:
            return self.project_keys[key]
        return self.application_keys[key]
