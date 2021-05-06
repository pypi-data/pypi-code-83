import os
import re
import pickle
import datetime

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.ERROR)


class Pickle:
    FILENAME = 'rno_anal_noti.pickle'
    FULL_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILENAME)

    @staticmethod
    def save(obj: dict):
        p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
        if p.match(obj['date']) is None:
            print(f"Invalid date - {obj['date']}(YYYYMMDD)")
            raise Exception
        logger.info(f'Save to pickle : {obj}')
        with open(Pickle.FULL_PATH, "wb") as fw:
            pickle.dump(obj, fw)

    @staticmethod
    def init(date: str):
        p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
        if p.match(date) is None:
            print(f'Invalid date - {date}(YYYYMMDD)')
            raise Exception
        logger.info(f'init {Pickle.FULL_PATH}')
        with open(Pickle.FULL_PATH, "wb") as fw:
            pickle.dump({'date': date, 'notified': [], 'analysed': []}, fw)

    @staticmethod
    def load() -> dict:
        try:
            with open(Pickle.FULL_PATH, "rb") as fr:
                obj = pickle.load(fr)
                logger.info(f'Load from pickle : {obj}')
                return obj
        except (EOFError, FileNotFoundError) as e:
            logger.error(e)
            Pickle.init(datetime.datetime.today().strftime('%Y%m%d'))
            with open(Pickle.FULL_PATH, "rb") as fr:
                obj = pickle.load(fr)
                logger.info(f'Load from pickle : {obj}')
                return obj

