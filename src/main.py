from ingestation.modules.configs.config import MergedConf
from ingestation.modules.misc.arguments import CliInput
from ingestation.modules.misc.utils import InitParams, Notify
from ingestation.modules.outputs import blocks
from ingestation.modules.outputs.loggers import Loggers


def main(cli_options: dict) -> None:
    init_params = InitParams()
    loggers = Loggers(cli_options)
    logger = loggers.logger

    blocks.log_starting_messages(logger, init_params, cli_options)

    config = MergedConf(logger, cli_options)
    logger.debug(config.final)

    if cli_options["notification"]:
        notify = Notify(config.final["notify"], loggers)
        notify.send_notifications(config.final["smtp"], "mail content")


def ingestation():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    ingestation()
