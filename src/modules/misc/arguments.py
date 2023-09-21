from argparse import ArgumentParser, Namespace
from re import fullmatch
from typing import Optional, Tuple, Union


class CliInput:

    option_names = {
        "debug": ["--debug", "-d"],
        "exclude": ["--exclude", "-e"],
        "include": ["--include", "-i"],
        "operator_conf": ["--operator-conf", "-c"],
        "project_conf": ["--project-conf", "-p"],
        "verification": ["--no-verification", "-n"]
    }

    short_args = "".join(list(short[1].strip("-") for short in option_names.values()))
    short_args_len = len(short_args)
    short_args_pattern = rf"[{short_args}]{{1,{short_args_len}}}"

    def create_parser(self) -> ArgumentParser:
        parser = ArgumentParser()

        parser.add_argument(self.option_names["debug"][0], self.option_names["debug"][1],
                            action="store_true", default=False, help="Start in debug mode.")
        parser.add_argument(self.option_names["exclude"][0], self.option_names["exclude"][1],
                            nargs="+", default=None, metavar=("DISK_SN_1", "DISK_SN_2"), help=
                            "Provide list (serial numbers, space separated) of containers to skip."
                            " Mutually exclusive with --include option.")
        parser.add_argument(self.option_names["include"][0], self.option_names["include"][1],
                            nargs="+", default=None, metavar=("DISK_SN_1", "DISK_SN_2"), help=
                            "Provide list (serial numbers, space separated) of containers to"
                            " process (others will be skipped). Mutually exclusive with --exclude"
                            " option.")
        parser.add_argument(self.option_names["operator_conf"][0], self.option_names[
                            "operator_conf"][1], nargs=1, default=None, metavar="PATH",
                            help="Load operator config file from provided PATH.")
        parser.add_argument(self.option_names["project_conf"][0], self.option_names[
                            "project_conf"][1], nargs=1, default=None, metavar="PATH",
                            help="Load project config file from provided PATH.")
        parser.add_argument(self.option_names["verification"][0], self.option_names["verification"]
                            [1], action="store_false", default=True, dest="verification", help=
                            "Specify that you want to skip verification step.")

        return parser

    def parse_arguments(self) -> dict:
        return self.validate_arguments(self.create_parser().parse_args())

    def validate_arguments(self, arguments: Namespace) -> dict:
        exclude_list, include_list = self.validate_inex_lists(arguments.exclude, arguments.include)

        return {
            "debug": arguments.debug,
            "exclude": exclude_list,
            "include": include_list,
            "operator_conf": self.validate_conf_path(arguments.operator_conf),
            "project_conf": self.validate_conf_path(arguments.project_conf),
            "verification": arguments.verification
        }

    def validate_inex_lists(self, exclude: list, include: list) -> Tuple:
        if exclude and include:
            raise TypeError("[CRITICAL]: Mutually exclusive lists were provided, use --help."
                            " Program will exit now.")

        return self.validate_inex_list(exclude), self.validate_inex_list(include)

    def validate_inex_list(self, input_list: list) -> Union[list, bool]:
        try:
            first = input_list[0]
        except TypeError:
            return False

        if len(first) < self.short_args_len and fullmatch(self.short_args_pattern, first):
            raise TypeError("[CRITICAL]: Short options concatenation is not allowed. Program"
                            " will exit now.")

        return self.create_list(input_list)

    @staticmethod
    def create_list(input_list: list) -> list:
        output_list = []
        for serial in input_list:
            output_list.append(serial.upper())

        return output_list

    @staticmethod
    def validate_conf_path(conf_path: Optional[str]) -> Union[str, bool]:
        if conf_path:
            try:
                open(conf_path[0])
                return conf_path[0]
            except Exception as exc:
                raise exc
        else:
            return False
