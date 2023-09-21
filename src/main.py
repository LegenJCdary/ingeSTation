from modules.configs.configs import MergedConf
from modules.misc.arguments import CliInput
from modules.misc import utils
from modules.outputs import blocks, logging


def main(cli_options: dict) -> None:
    init_params = utils.InitParams()
    loggers = logging.Loggers(cli_options)
    logger = loggers.logger
    log_blocks = blocks.Blocks(logger)
    log_blocks.log_starting_messages(init_params, cli_options)

    config = MergedConf(logger, cli_options)
    log_blocks.log_loaded_configs(config)


def cargoloader():
    return main(CliInput.parse_arguments(CliInput()))


if __name__ == "__main__":
    cargoloader()
