import logging
import os
import pytest
from jsonschema import ValidationError

from src.modules.configs import schemas
from src.modules.configs.config import Conf, MergedConf
from src.modules.global_vars import APPLICATION_DIR
from tests.data import test_results
from tests.data import test_data

current_path = os.path.join(os.path.dirname(__file__))
test_data_path = os.path.join(os.path.dirname(os.path.dirname(current_path)), "data")


class TestConf:
    """Class to test functions of Conf class"""

    def test_validate_conf_app(self):
        app = Conf("", "application", schemas.application)
        assert app.validate_conf(test_data.validate_app) is None

    def test_validate_conf_proj(self):
        app = Conf("", "project", schemas.project)
        assert app.validate_conf(test_data.validate_proj) is None

    def test_validate_conf_op(self):
        app = Conf("", "operator", schemas.operator)
        assert app.validate_conf(test_data.validate_op) is None

    def test_validate_conf_error(self):
        op = Conf("", "operator", schemas.operator)
        op_dct = test_data.validate_op_error

        with pytest.raises(ValidationError) as exinfo:
            op.validate_conf(op_dct)
        assert exinfo.type == ValidationError

    def test_get_conf_path_conf_path_str(self):
        app = Conf(os.path.join(test_data_path, "app.json"), "application", schemas.application)
        assert app.get_conf_path("/test_path") == "/test_path"

    def test_get_conf_path_conf_path_bool(self):
        app = Conf(os.path.join(test_data_path, "app.json"), "application", schemas.application)
        conf_file_here = os.path.join(os.getcwd(), f"{app.conf_type}.json")
        assert app.get_conf_path("") == conf_file_here

    def test_get_conf_path_app_dir(self):
        proj = Conf(os.path.join(test_data_path, "proj.json"), "project", schemas.project)
        assert proj.get_conf_path("") == \
               os.path.join(APPLICATION_DIR, f"{proj.conf_type}.json")


class TestMergedConf:
    """Class to test functions of MergedConf class"""

    def test_flatten_dict_simple_dict(self):
        mconf = MergedConf(logging.getLogger())

        dct = test_data.flatten_dict_simple
        assert mconf.flatten_dict(dct) == test_results.flatten_simple_dict_result

    def test_flatten_dict_complex_dict(self):
        mconf = MergedConf(logging.getLogger())

        dct = test_data.flatten_dict_complex
        assert mconf.flatten_dict(dct, sep="#", exclude_keys=["d"]) == \
               test_results.flatten_complex_dict_result

    def test_create_final_conf_success(self):
        mconf = MergedConf(logging.getLogger())

        assert mconf.create_final_conf() == test_results.final_conf

    def test_create_final_conf_exception(self):
        ex_msg = "Missing mandatory value of: destination_root_path"
        with pytest.raises(Exception) as exinfo:
            mconf = MergedConf(logging.getLogger())
            mconf.create_final_conf()
        assert exinfo.type == Exception
        assert str(exinfo.value) == ex_msg
