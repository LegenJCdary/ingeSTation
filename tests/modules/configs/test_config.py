import logging
import os
import pytest
from jsonschema import ValidationError

from src.modules.global_vars import OPTIONS
from src.modules.configs.config import Conf, MergedConf
from tests.data import test_results
from tests.data import test_data

current_path = os.path.join(os.path.dirname(__file__))
test_data_path = os.path.join(os.path.dirname(os.path.dirname(current_path)), "data")


class TestConf:
    """Class to test functions of Conf class"""

    def test_validate_conf_app(self):
        app = Conf("", "application")
        assert app.validate_conf(test_data.validate_app) is None

    def test_validate_conf_proj(self):
        app = Conf("", "project")
        assert app.validate_conf(test_data.validate_proj) is None

    def test_validate_conf_op(self):
        app = Conf("", "operator")
        assert app.validate_conf(test_data.validate_op) is None

    def test_validate_conf_error(self):
        op = Conf("", "operator")
        op_dct = test_data.validate_op_error

        with pytest.raises(ValidationError) as exinfo:
            op.validate_conf(op_dct)
        assert exinfo.type == ValidationError

    def test_get_conf_path_conf_path_str(self):
        app = Conf(os.path.join(test_data_path, "app.json"), "application")
        assert app.get_conf_path("/test_path") == "/test_path"

    def test_get_conf_path_conf_path_bool(self):
        app = Conf(os.path.join(test_data_path, "app.json"), "application")
        conf_file_here = os.path.join(os.getcwd(), f"{app.conf_type}.json")
        assert app.get_conf_path("") == conf_file_here

    def test_get_conf_path_app_dir(self):
        proj = Conf(os.path.join(test_data_path, "proj.json"), "project")
        assert proj.get_conf_path("") == \
               os.path.join(global_vars.APPLICATION_DIR, f"{proj.conf_type}.json")

    def test_get_conf_path_file_not_found(self):
        test = Conf(os.path.join(test_data_path, "test.json"), "test")
        with pytest.raises(FileNotFoundError) as exinfo:
            test.get_conf_path("")
        assert exinfo.type == FileNotFoundError


class TestMergedConf:
    """Class to test functions of MergedConf class"""

    def test_flatten_dict_simple_dict(self):
        mconf = MergedConf(logging.getLogger(), global_vars.options)

        dct = test_data.flatten_dict_simple
        assert mconf.flatten_dict(dct) == test_results.flatten_simple_dict_result

    def test_flatten_dict_complex_dict(self):
        mconf = MergedConf(logging.getLogger(), global_vars.options)

        dct = test_data.flatten_dict_complex
        assert mconf.flatten_dict(dct, sep="#", exclude_keys=["d"]) == \
               test_results.flatten_complex_dict_result

    def test_create_final_conf_success(self):
        test_options = {
            "application_conf": os.path.join(test_data_path, "app.json"),
            "project_conf": os.path.join(test_data_path, "proj.json"),
            "operator_conf": os.path.join(test_data_path, "op.json")
        }
        mconf = MergedConf(logging.getLogger(), test_options)

        assert mconf.create_final_conf() == test_results.final_conf

    def test_create_final_conf_exception(self):
        test_options = {
            "application_conf": os.path.join(test_data_path, "app.json"),
            "project_conf": os.path.join(test_data_path, "proj2.json"),
            "operator_conf": os.path.join(test_data_path, "op.json")
        }
        ex_msg = "Missing mandatory value of: destination_root_path"
        with pytest.raises(Exception) as exinfo:
            mconf = MergedConf(logging.getLogger(), test_options)
            mconf.create_final_conf()
        assert exinfo.type == Exception
        assert str(exinfo.value) == ex_msg
