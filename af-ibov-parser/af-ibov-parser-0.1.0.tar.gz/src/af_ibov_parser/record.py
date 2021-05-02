'''
This module is responsible for serializing
raw ibov data into python objects.
'''


import hashlib

import canonicaljson  # type:ignore


def str2(s: str) -> str:
    '''
    Returns a string removing any
    blank spaces at the end of the string.
    '''
    return s.rstrip(' ')


def str2int(s: str) -> int:
    '''
    Parses a string into a integer.

    It removes any `0` chars at the start of the string.

    Returns `0` in case a ` ValueError` is raised.
    '''
    parsed = s.lstrip('0').strip()
    try:
        return int(parsed)
    except ValueError:
        return 0


class Record:
    '''
    Record class that serializes an
    ibov record from a string into
    a record instance.
    '''

    def __init__(self, regtype: str, date: str, bdi_code: str, ticker: str,
                 market: str, company_short_name: str, category: str,
                 time_period: str, currency: str, price_openning: str,
                 price_highest: str, price_lowest: str, price_average: str,
                 price_last: str, price_bid_best: str, price_ask_best: str,
                 deals_total: str, transactions_total: str, volume_total: str,
                 price_strike: str, price_correction_ref: str,
                 expiration_date: str, batch: str,
                 price_strike_points: str, isin_id: str, dismes: str) -> None:
        '''
        Creates a new record insance.

        All fields are mandatory.
        '''
        self.regtype = regtype
        self.date = date
        self.bdi_code = bdi_code
        self.ticker = str2(ticker)
        self.market = market
        self.company_short_name = str2(company_short_name)
        self.category = str2(category)
        self.time_period = str2int(time_period)
        self.currency = str2(currency)
        self.price_openning = str2int(price_openning)
        self.price_highest = str2int(price_highest)
        self.price_lowest = str2int(price_lowest)
        self.price_average = str2int(price_average)
        self.price_last = str2int(price_last)
        self.price_bid_best = str2int(price_bid_best)
        self.price_ask_best = str2int(price_ask_best)
        self.deals_total = str2int(deals_total)
        self.transactions_total = str2int(transactions_total)
        self.volume_total = str2int(volume_total)
        self.price_strike = str2int(price_strike)
        self.price_correction_ref = str2int(price_correction_ref)
        self.expiration_date = expiration_date
        self.batch = str2int(batch)
        self.price_strike_points = str2int(price_strike_points)
        self.isin_id = isin_id
        self.dismes = dismes

    @classmethod
    def from_str(cls, data: str) -> 'Record':
        '''
        Return a new record instance from
        a record raw str.
        '''
        return cls(
            data[0:2],
            data[2:10],
            data[10:12],
            data[12:24],
            data[24:27],
            data[27:39],
            data[39:49],
            data[49:52],
            data[52:56],
            data[56:69],
            data[69:82],
            data[82:95],
            data[95:108],
            data[108:121],
            data[121:134],
            data[134:147],
            data[147:152],
            data[152:170],
            data[171:188],
            data[188:201],
            data[201:202],
            data[202:210],
            data[210:217],
            data[217:230],
            data[230:242],
            data[242:245]
        )

    def as_json(self) -> str:
        '''
        Return a json string repsentation
        of a record.
        '''
        return str(canonicaljson.encode_canonical_json({
            'regtype': self.regtype,
            'date': self.date,
            'bdi_code': self.bdi_code,
            'ticker': self.ticker,
            'market': self.market,
            'company_short_name': self.company_short_name,
            'category': self.category,
            'time_period': self.time_period,
            'currency': self.currency,
            'price_openning': self.price_openning,
            'price_highest': self.price_highest,
            'price_lowest': self.price_lowest,
            'price_average': self.price_average,
            'price_last': self.price_last,
            'price_bid_best': self.price_bid_best,
            'price_ask_best': self.price_ask_best,
            'deals_total': self.deals_total,
            'transactions_total': self.transactions_total,
            'volume_total': self.volume_total,
            'price_strike': self.price_strike,
            'price_correction_ref': self.price_correction_ref,
            'expiration_date': self.expiration_date,
            'batch': self.batch,
            'price_strike_points': self.price_strike_points,
            'isin_id': self.isin_id,
            'dismes': self.dismes
        }).decode())

    def as_hash(self) -> str:
        '''
        Return a sha256 hash representation of the object.

        It will generate the hash from `self.as_json()`.
        '''
        return str(hashlib.sha256(self.as_json().encode()).hexdigest())
