#from configCore import *
import logging





def GetBrahmaLogger(source='undef'):
    """[summary]

    Args:
        source (str, optional): Source module/class of log message. Defaults to 'undef'.

    Returns:
        logger: logger handle
    """
    
    # define BRAHMA_CORE_LOG_PATH
    import os
    
    BRAHMA_CORE_LOG_PATH = os.environ['BRAHMA_APP_LOG_PATH']

    # create logger with 'spam_application'
    logger = logging.getLogger(source)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler with a higher log level
    fh = logging.FileHandler(BRAHMA_CORE_LOG_PATH + "brahmalog.txt", 'a')
    fh.setLevel(logging.DEBUG)

    #format logging
    ch.setFormatter(BrahmaLogFormatter())
    fh.setFormatter(BrahmaLogFormatter())

    #set logging level
    logger.setLevel(logging.DEBUG)

    #attach streams to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


class BrahmaLogFormatter(logging.Formatter):
  """
  BrahamLogger provides the formatting required for all logging
  in brahmaCore. 

  Args:
      Level (String): Level of logging output {debug, error, ...}
  """
  grey = "\x1b[38;21m"
  yellow = "\x1b[33;21m"
  red = "\x1b[31;21m"
  bold_red = "\x1b[31;1m"
  reset = "\x1b[0m"
  format = "%(asctime)s - %(name)-20s - %(levelname)-10s - %(message)-40s (%(filename)s:%(lineno)d)"

  FORMATS = {
      logging.DEBUG: grey + format + reset,
      logging.INFO: grey + format + reset,
      logging.WARNING: yellow + format + reset,
      logging.ERROR: red + format + reset,
      logging.CRITICAL: bold_red + format + reset
  }

  def format(self, record):
      log_fmt = self.FORMATS.get(record.levelno)
      formatter = logging.Formatter(log_fmt)
      return formatter.format(record)

if __name__ == "__main__":
        
    # create logger with 'spam_application'
    logger = logging.getLogger("LoggingFormatter")

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler with a higher log level
    fh = logging.FileHandler(BRAHMA_CORE_LOG_PATH + "log.txt", 'w+')
    fh.setLevel(logging.DEBUG)



    if len(sys.argv)> 1:
        if sys.argv[1] == 'log':
            ch.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s'))
            fh.setFormatter(logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s'))
            
        elif sys.argv[1] == 'color':
            ch.setFormatter(BrahmaLogFormatter())
            fh.setFormatter(BrahmaLogFormatter())

    if len(sys.argv) > 2:
        logger.setLevel(logging.__getattribute__(sys.argv[2]))
    else:
        logger.setLevel(logging.DEBUG)

    logger.addHandler(ch)
    logger.addHandler(fh)


    import random
    import time
    for _ in range(100):
        i = random.randint(0, 10)
        if i <= 4:
            logger.info("Value is {} - Everything is fine".format(i))
        elif i <= 6:
            logger.warning("Value is {} - System is getting hot".format(i))
        elif i <= 8:
            logger.error("Value is {} - Dangerous region".format(i))
        else:
            logger.critical("Maximum value reached")
        time.sleep(0.3)
