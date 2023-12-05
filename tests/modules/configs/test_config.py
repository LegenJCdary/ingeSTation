import os
import pytest

from jsonschema import ValidationError

from ingestation.modules.configs.config import ApplicationConf, ProjectConf, OperatorConf, \
    validate_json
from ingestation.modules.configs.schemas import application, project, operator
from ingestation.modules.global_vars import APPLICATION_DIR
from ingestation_test.data.configs import validate_json_passed, validate_json_failed, \
    error_messages as err_msg


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

    @pytest.mark.parametrize("conf_type,conf", [("application", ApplicationConf("")),
                                                ("project", ProjectConf("")),
                                                ("operator", OperatorConf(""))])
    def test_get_conf_path_application_dir(self, conf_type, conf):
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
