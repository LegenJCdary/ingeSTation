from ingestation.modules.misc.arguments import CliInput
from ingestation.modules.misc.utils import InitParams
from ingestation.modules.outputs.loggers import Loggers
from ingestation.modules.outputs import blocks


def main(cli_options: dict) -> None:
    init_params = InitParams()
    loggers = Loggers(cli_options)
    logger = loggers.logger

    blocks.log_starting_messages(logger, init_params, cli_options)


def ingestation():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    ingestation()
