import logging

levelmap = {
    "low": logging.DEBUG,
    "medium": logging.INFO,
    "high": logging.WARNING
}


def configure_logger(log_level, log_file):
    log_level = levelmap[log_level]
    log_format = '%(asctime)s [%(levelname)s] %(message)s'
    handler_list = [
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
    logging.basicConfig(level=log_level, format=log_format, handlers=handler_list)
