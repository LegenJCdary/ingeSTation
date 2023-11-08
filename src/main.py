from ingestation.modules.misc.arguments import CliInput
from ingestation.modules.misc.utils import InitParams
from ingestation.modules.outputs.loggers import Loggers


def main(cli_options: dict) -> None:
    init_params = InitParams()
    init_attrs = \
        [attr for attr in dir(init_params) if not any(attr.startswith(x) for x in ["_", "get"])]
    print_params = ", ".join([str(getattr(init_params, attr)) for attr in init_attrs])
    print_options = ", ".join([f"{k}={v}" for k, v in cli_options.items()])
    print("Welcome to ingeSTation project!")
    print(f"Started with: {print_params}")
    print(f"Supplied options: {print_options}")
    loggers = Loggers(cli_options)
    logger = loggers.logger


def ingestation():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    ingestation()
