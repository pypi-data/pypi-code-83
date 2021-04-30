from ciocore import common, loggeria

try:
    CONFIG = common.Config().config
except ValueError:
    CONFIG = common.Config().config


# Must setup logging before setting the level, otherwise we get an
# annoying complaint about no handlers for logger conductor.
log_level_name = CONFIG.get("log_level", "INFO")
log_level = loggeria.LEVEL_MAP.get(log_level_name)
loggeria.setup_conductor_logging(
    logger_level=log_level, 
    console_formatter=loggeria.FORMATTER_VERBOSE
)
