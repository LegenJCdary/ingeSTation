from logging import Logger

from ingestation.modules.misc.utils import InitParams


def log_starting_messages(logger: Logger, init_params: InitParams, cli_options: dict) -> None:
    start_point = init_params.start_point.strftime("%a %d %b %Y, %H:%M:%S")
    logger.info(f"Welcome to ingeSTation {init_params.caller_name}!")
    logger.info(f"Starting at {start_point} on {init_params.hostname}.")
    logger.debug("Command line options are:")
    for key, val in cli_options.items():
        val_string = " ".join(val) if isinstance(val, (list, dict)) else val
        logger.debug(f"\t{key}\t\t{val_string}")
