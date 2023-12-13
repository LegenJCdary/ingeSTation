import pytest

from jsonschema import ValidationError

from ingestation.modules.configs.config import validate_json
from ingestation.modules.configs.schemas import application, project, operator
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
