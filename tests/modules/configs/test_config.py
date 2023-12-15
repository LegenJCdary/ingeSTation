import os

import pytest
from jsonschema import ValidationError

from ingestation.modules.configs.config import ApplicationConf, ProjectConf, OperatorConf, \
    MergedConf, validate_json
from ingestation.modules.configs.schemas import application, project, operator
from ingestation.modules.global_vars import APPLICATION_DIR
from ingestation.modules.outputs.loggers import Loggers
from ingestation_test.data.configs import validate_json_passed, validate_json_failed, err_msg, \
    merge_conf, config_rule


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_unrecognized_key(conf_type: str, schema):
    full_conf = getattr(validate_json_failed, conf_type)
    conf = full_conf.get("unrecognized_key")

    with pytest.raises(ValidationError) as ex:
        validate_json(conf, schema)
    assert err_msg.validate_json.get("unrecognized_key") in str(ex.value)


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_mandatory_key(conf_type: str, schema):
    full_conf = getattr(validate_json_failed, conf_type)
    conf = full_conf.get("mandatory_key")

    with pytest.raises(ValidationError) as ex:
        validate_json(conf, schema)
    assert err_msg.validate_json.get("mandatory_key") in str(ex.value)


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_invalid_data_type(conf_type: str, schema):
    full_conf = getattr(validate_json_failed, conf_type)
    conf = full_conf.get("invalid_data_type")

    with pytest.raises(ValidationError) as ex:
        validate_json(conf, schema)
    assert err_msg.validate_json.get("invalid_data_type") in str(ex.value)


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_too_long_value(conf_type: str, schema):
    full_conf = getattr(validate_json_failed, conf_type)
    conf = full_conf.get("too_long_value")

    with pytest.raises(ValidationError) as ex:
        validate_json(conf, schema)
    assert err_msg.validate_json.get("too_long_value") in str(ex.value)


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_non_mandatory_key(conf_type: str, schema):
    full_conf = getattr(validate_json_passed, conf_type)
    conf = full_conf.get("non_mandatory_key")

    assert validate_json(conf, schema) is None


@pytest.mark.parametrize("conf_type,schema", [
    ["application", application],
    ["project", project],
    ["operator", operator],
])
def test_validate_json_validation_passed(conf_type: str, schema):
    full_conf = getattr(validate_json_passed, conf_type)
    conf = full_conf.get("validation_passed")

    assert validate_json(conf, schema) is None


class TestConf:
    """Class to test functions of Conf class"""
    current_path = os.path.join(os.path.dirname(__file__))
    test_data_path = os.path.join(os.path.dirname(os.path.dirname(current_path)),
                                  "data", "configs")

    @pytest.mark.parametrize("conf_type", ["application", "project", "operator"])
    def test_get_conf_path_application_dir(self, conf_type):
        if conf_type == "application":
            conf = ApplicationConf("")
        elif conf_type == "project":
            conf = ProjectConf("")
        else:
            conf = OperatorConf("")
        assert conf.get_conf_path("") == os.path.join(APPLICATION_DIR, f"{conf_type}.json")

    def test_get_conf_path_file_found(self):
        conf_path = os.path.join(self.test_data_path, "application.json")
        conf = ApplicationConf(conf_path)
        assert conf_path == conf.get_conf_path(conf_path)

    def test_get_conf_path_file_not_found(self):
        conf_path = os.path.join(self.test_data_path, "project.json")
        with pytest.raises(FileNotFoundError) as ex:
            conf = ProjectConf(conf_path)
            conf.get_conf_path(conf_path)
        assert ex.type == FileNotFoundError
        assert err_msg.get_conf_path.get("file_not_found") in str(ex.value)


class TestMergedConf:
    """Class to test functions of MergedConf Class"""

    @staticmethod
    def none_to_dict(obj):
        if obj is None:
            return {}
        return obj

    @pytest.mark.parametrize("dct, expect", [
        [merge_conf.dct1, merge_conf.expect1],
        [merge_conf.dct2, merge_conf.expect2],
        [merge_conf.dct3, merge_conf.expect3],
    ])
    def test_merge_conf(self, dct, expect):
        conf = MergedConf(Loggers({}))
        assert conf.merge_conf(dct) == expect

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["resources_thread_count", "exclusive_over_defined"]
    ])
    def test_apply_config_rule_exclusive_over_defined(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }
        error_message = err_msg.apply_config_rule.get(rule_type)

        with pytest.raises(Exception) as ex:
            config.apply_config_rule(merged_key)
        assert error_message in str(ex)

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["resources_thread_count", "exclusive_undefined"]
    ])
    def test_apply_config_rule_exclusive_undefined(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }

        assert config.apply_exclusive_rule(merged_key) is None

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["containers_sata_device_path", "exclusive_passed"],
    ])
    def test_apply_config_rule_exclusive_passed(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }

        assert config.apply_exclusive_rule(merged_key) == config_rule.result.get(rule_type)

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["notify", "inclusive_passed"],
    ])
    def test_apply_config_rule_inclusive_passed(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }

        assert sorted(config.apply_inclusive_rule(merged_key)) \
               == sorted(config_rule.result.get(rule_type))

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["workdir", "priority_passed"],
    ])
    def test_apply_config_rule_priority_passed(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }

        assert config.apply_priority_rule(merged_key) == config_rule.result.get(rule_type)

    @pytest.mark.parametrize("merged_key, rule_type", [
        ["destination_type", "priority_none"],
    ])
    def test_apply_config_rule_priority_none(self, merged_key, rule_type):
        config = MergedConf(Loggers({}))

        app = config_rule.application.get(rule_type)
        prj = config_rule.project.get(rule_type)
        op = config_rule.operator.get(rule_type)

        config.merged_confs = {
            "application": config.merge_conf(self.none_to_dict(app)),
            "project": config.merge_conf(self.none_to_dict(prj)),
            "operator": config.merge_conf(self.none_to_dict(op))
        }

        assert config.apply_priority_rule(merged_key) is None
