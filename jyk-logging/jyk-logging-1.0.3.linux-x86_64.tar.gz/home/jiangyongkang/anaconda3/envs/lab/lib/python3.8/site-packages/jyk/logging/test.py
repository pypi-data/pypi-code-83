import logging

log = logging.getLogger(__name__)


def makeLogs():
    for i in range(3):
        log.info("test log info {}".format(i))
    for i in range(3):
        log.warning("test log warning {}".format(i))
    for i in range(3):
        log.error("test log error {}".format(i))
