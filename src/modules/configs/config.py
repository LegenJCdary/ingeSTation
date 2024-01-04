import os
from json import loads
from typing import Union

from jsonschema import validate, ValidationError

from ingestation.modules.configs.schemas import application, project, operator, \
    final as final_schema
from ingestation.modules.configs.templates import final
from ingestation.modules.global_vars import APPLICATION_DIR, CONFIG_RULES
from ingestation.modules.outputs.loggers import Loggers


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


class ConfigRulesError(Exception):
    pass


class ConfigFilesError(Exception):
    pass


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


class MergedConf:
    def __init__(self, logger: Loggers, cli_options: dict):
        self.logger = logger
        self.application = ApplicationConf("").parse_conf()
        self.project = ProjectConf("").parse_conf()
        self.operator = OperatorConf("").parse_conf()
        self.cli_options = cli_options

        self.merged_confs = {
            "cli": self.parse_cli_options(),
            "application": self.merge_conf(self.application),
            "project": self.merge_conf(self.project),
            "operator": self.merge_conf(self.operator)
        }

        self.merged_conf = self.create_merged_conf()
        self.final = self.create_final_conf()

    @staticmethod
    def extract_dict_keys(dct):
        keys = []

        for key, value in dct.items():
            keys.append(key)
            if isinstance(value, dict):
                sub_keys = MergedConf.extract_dict_keys(value)
                keys.extend(sub_keys)

        return keys

    @staticmethod
    def replace_str_in_list(lst: list, old_str, new_str):
        for s in lst:
            if old_str in s:
                new_s = str.replace(s, old_str, new_str)
                lst.remove(s)
                lst.append(new_s)
        return lst

    @staticmethod
    def add_values_to_dict_keys(dct, keys, value):
        if len(keys) == 1:
            dct[keys[0]] = value
        else:
            key = keys[0]
            if key not in dct:
                dct[key] = {}
            MergedConf.add_values_to_dict_keys(dct[key], keys[1:], value)

    def parse_cli_options(self):
        cli = {}
        for k, v in self.cli_options.items():
            if k in CONFIG_RULES:
                cli[k] = v
        return cli

    def create_merged_conf(self):
        merged_conf = self.merge_conf(final.template)
        rule_mode = ("exclusive", "inclusive", "priority")
        rule_order = ("application", "project", "operator", "cli")

        for key, value in CONFIG_RULES.items():
            rule = CONFIG_RULES.get(key)
            if not rule:
                raise ConfigRulesError(f"No rules defined for conf key ({key}). "
                                       f"Update CONFIG_RULES.")
            mode = value.get("mode")
            if not mode:
                raise ConfigRulesError(
                    f"Mode is undefined. "
                    f"Rule mode for key ({key}) needs to be defined for rule mode. "
                    f"Update CONFIG_RULES."
                )
            if mode not in rule_mode:
                raise ConfigRulesError(
                    f"Invalid mode ({mode}) in key ({key}) is defined. "
                    f"Rule mode must be one of {rule_mode}. Update CONFIG_RULES."
                )

            order = value.get(mode)
            if not order:
                raise ConfigRulesError(
                    f"Order is undefined. "
                    f"Rule order for key ({key}) needs to be defined for rule mode. "
                    f"Update CONFIG_RULES."
                )
            for odr in order:
                if odr not in rule_order:
                    raise ConfigRulesError(
                        f"Invalid order ({odr}) in key ({key}) is defined. "
                        f"Rule order must be one of {rule_order}. Update CONFIG_RULES."
                    )
            merged_conf[key] = self.get_final_value(key)

        return merged_conf

    def get_final_value(self, merged_key):
        value = self.apply_config_rule(merged_key)

        if value is None:
            return CONFIG_RULES[merged_key].get("default")

        return value

    def apply_config_rule(self, merged_key):
        mode = CONFIG_RULES.get(merged_key).get("mode")

        if mode == "exclusive":
            value = self.apply_exclusive_rule(merged_key)
        elif mode == "inclusive":
            value = self.apply_inclusive_rule(merged_key)
        else:
            value = self.apply_priority_rule(merged_key)

        return value

    def merge_conf(self, dct):
        merged_conf = {}

        for key, value in dct.items():
            if isinstance(value, dict):
                nested = self.merge_conf(value)
                for nested_key, nested_value in nested.items():
                    merged_conf[f"{key}_{nested_key}"] = nested_value
            else:
                merged_conf[key] = value

        return merged_conf

    def create_final_conf(self):
        final_extracted_keys = MergedConf.extract_dict_keys(final.template)
        final_conf = {}
        excluded_keys = []

        for key in final_extracted_keys:
            if "_" in key:
                excluded_keys.append(key)

        for key, value in self.merged_conf.items():
            for ex_key in excluded_keys:
                if ex_key in key:
                    new_ex_key = str.replace(ex_key, "_", "-")
                    key = str.replace(key, ex_key, new_ex_key)
                    break
            separated_key = str.split(key, "_")
            separated_key = MergedConf.replace_str_in_list(separated_key, "-", "_")
            MergedConf.add_values_to_dict_keys(final_conf, separated_key, value)

        validate_json(final_conf, final_schema)

        return final_conf

    def apply_exclusive_rule(self, merged_key):
        """
        1. Check if value is defined in both -> raise Exc
        2. Return value if defined in any
        3. If undefined -> return None
        """
        order = CONFIG_RULES.get(merged_key)["exclusive"]
        value_count = 0
        value, effective_value = None, None

        for config in order:
            value = self.merged_confs[config].get(merged_key)
            if value:
                value_count += 1
                effective_value = value
            if value_count > 1:
                raise ConfigFilesError(
                    f"{merged_key} is defined in more than one config: {str(order)}"
                )

        return effective_value

    def apply_inclusive_rule(self, merged_key):
        """Just merge all of them (remove duplicates)"""
        order = CONFIG_RULES.get(merged_key)["inclusive"]
        merged_value = []

        for conf in order:
            value = self.merged_confs[conf].get(merged_key)
            if value:
                merged_value.extend(value)

        return list(set(merged_value))

    def apply_priority_rule(self, merged_key):
        """
        Cascade/iterate conf by conf using defined order
        If undefined at the end, return None
        """
        order = CONFIG_RULES.get(merged_key)["priority"]

        for conf in order:
            value = self.merged_confs[conf].get(merged_key)
            if value is not None:
                return value

        return None
