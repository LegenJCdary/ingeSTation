from argparse import ArgumentParser, Namespace
from re import fullmatch
from typing import Tuple, Union


class CliInput:
    """
    Command-line interface handler.

    Collects, parses and validates arguments passed on execution.
    """

    option_names = {
        "debug": ["--debug", "-d"],
        "exclude": ["--exclude", "-e"],
        "include": ["--include", "-i"],
        "verification": ["--no-verification", "-n"],
        "notification": ["--no-notification", "-m"]
    }

    short_args = "".join([short[1].strip("-") for short in option_names.values()])
    short_args_len = len(short_args)
    short_args_pattern = rf"[{short_args}]{{1,{short_args_len}}}"

    def create_parser(self) -> ArgumentParser:
        parser = ArgumentParser()

        parser.add_argument(self.option_names["debug"][0], self.option_names["debug"][1],
                            action="store_true", default=False,
                            help="Start ingeSTation in debug mode.")
        parser.add_argument(self.option_names["exclude"][0], self.option_names["exclude"][1],
                            nargs="+", default=None, metavar=("DEVICE_ID_1", "DEVICE_ID_2"), help=
                            "Provide space-separated, serial numbers list of devices to skip."
                            " Mutually exclusive with --include option.")
        parser.add_argument(self.option_names["include"][0], self.option_names["include"][1],
                            nargs="+", default=None, metavar=("DEVICE_ID_1", "DEVICE_ID_2"), help=
                            "Provide space-separated, serial numbers list of devices to process"
                            " (others will be skipped). Mutually exclusive with --exclude option.")
        parser.add_argument(self.option_names["verification"][0], self.option_names["verification"]
                            [1], action="store_false", default=True, dest="verification", help=
                            "Skip verification step performed after data ingest.")
        parser.add_argument(self.option_names["notification"][0], self.option_names["notification"]
                            [1], action="store_false", default=True, dest="notification", help=
                            "Skip notification step performed after data ingest.")

        return parser

    def parse_arguments(self) -> dict:
        return self.validate_arguments(self.create_parser().parse_args())

    def validate_arguments(self, arguments: Namespace) -> dict:
        exclude_list, include_list = self.validate_inex_lists(arguments.exclude, arguments.include)

        return {
            "debug": arguments.debug,
            "exclude": exclude_list,
            "include": include_list,
            "verification": arguments.verification,
            "notification": arguments.notification
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

        return self.create_sn_list(input_list)

    @staticmethod
    def create_sn_list(input_list: list) -> list:
        return [serial.upper() for serial in input_list]
