from ingestation.modules.misc.arguments import CliInput
from ingestation.modules.misc.utils import InitParams, Notify
from ingestation.modules.outputs.loggers import Loggers
from ingestation.modules.outputs import blocks
from ingestation.modules.mounting.mounting import Mounting
from ingestation.modules.partitioning.listing import DataPartiioning
from ingestation.modules.threading.working import Workers
from ingestation.modules.verification.verify import Verify


def main(cli_options: dict) -> None:
    init_params = InitParams()
    loggers = Loggers(cli_options)
    logger = loggers.logger

    blocks.log_starting_messages(logger, init_params, cli_options)

    configuration = MergedConfig(logger).config
    mela_plan = MOunting(configuration)
    bites = DataPartiioning(logger, configuration, docking_list)

    swallowed = Workers()
    if swallowed:
        verify = Verify()
        if configuration.notify:
            Notify().send_notification()


def ingestation():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    ingestation()
