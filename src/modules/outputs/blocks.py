from logging import Logger

from ..configs.configs import MergedConf
from ..misc.utils import InitParams, get_exec_modes


class Blocks:

    def __init__(self, logger: Logger):
        self.logger = logger

    def log_dict_elements(self, dictionary: dict, indent_level: int) -> None:
        indent = "\t" * indent_level

        for key, val in dictionary.items():
            try:
                if len(val) > 0:
                    if isinstance(val, str):
                        val_string = val
                    else:
                        self.logger.debug(f"{indent}{key}")
                        if isinstance(val, dict):
                            self.log_dict_elements(val, indent_level + 1)
                        else:
                            self.log_list_elements(val, indent_level + 1)
                        continue
                else:
                    val_string = "EMPTY"
            except TypeError:
                val_string = val

            self.logger.debug(f"{indent}{key}\t\t{val_string}")

    def log_list_elements(self, input_list: list, indent_level: int) -> None:
        indent = "\t" * indent_level
        counter = 1

        if isinstance(input_list[0], dict):
            for item in input_list:
                self.logger.debug(f"{indent}{counter}.")
                counter += 1
                self.log_dict_elements(item, indent_level + 1)
        elif isinstance(input_list[0], list):
            for item in input_list:
                self.logger.debug(f"{indent}{counter}.")
                counter += 1
                self.log_list_elements(item, indent_level + 1)
        else:
            fmt = "{}{}".format(indent, "{}; " * len(input_list)).strip("; ")
            self.logger.debug(fmt.format(*input_list))

    def log_starting_messages(self, init_params: InitParams, cli_options: dict) -> None:
        self.logger.info(f"Welcome to cargoloader {init_params.caller_name}!")
        self.logger.info(f"Starting at {init_params.start_point} on {init_params.hostname}.")
        self.logger.debug("Command line options are:")
        self.log_dict_elements(cli_options, 1)
        self.logger.info(f"Running following modes: {get_exec_modes(cli_options)}.")

    def log_loaded_configs(self, config: MergedConf) -> None:
        self.logger.debug("Application configuration:")
        self.log_dict_elements(config.application, 0)
        self.logger.debug("")
        self.logger.debug("Project configuration:")
        self.log_dict_elements(config.project, 0)
        self.logger.debug("")
        self.logger.debug("Operator configuration:")
        self.log_dict_elements(config.operator, 0)
        self.logger.debug("")
        self.logger.debug("Final configuration:")
        self.log_dict_elements(config.final, 0)
        self.logger.debug("")
