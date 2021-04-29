from argparse import ArgumentParser
from configparser import ConfigParser
from os import path

from coinbase.auth import CoinbaseAuth
from coinbase.const import SUPPORTED_CURRENCIES
from coinbase.mgmt import PortfolioMgmt


def read_ini_file(path: str):
    config = ConfigParser()
    config.read(path)
    return config


def confirmation():
    if input("Are you sure ? [Y/n]") not in ["Y", "y"]:
        exit(1)


def execute_from_commandline():
    api_url = "https://api.coinbase.com/v2/"
    parser = ArgumentParser()
    parser.add_argument('--config', type=str,
                        help="The path of your configuration file")
    subparsers = parser.add_subparsers(help="Coinbase CLI commands")
    price_parser = subparsers.add_parser("price")
    buy_parser = subparsers.add_parser("buy")
    sell_parser = subparsers.add_parser("sell")
    wallet_parser = subparsers.add_parser("wallet")
    balance_parser = subparsers.add_parser("balance")
    price_parser.add_argument("p_currency", type=str,
                              choices=SUPPORTED_CURRENCIES)
    buy_parser.add_argument("currency", type=str, choices=SUPPORTED_CURRENCIES)
    sell_parser.add_argument("currency", type=str,
                             choices=SUPPORTED_CURRENCIES)
    wallet_parser.add_argument(
        "w_currency", type=str, choices=SUPPORTED_CURRENCIES)
    balance_parser.add_argument(
        "b_currency", type=str, choices=SUPPORTED_CURRENCIES)

    args = parser.parse_args()
    if args.config is not None:
        conf = read_ini_file(args.config)
    else:
        conf = read_ini_file(path.join(path.dirname(path.dirname(__file__)),"config.ini"))

    try:
        print("Connecting to Coinbase...")
        API_KEY = conf["coinbase"]["public"]
        API_SECRET = conf["coinbase"]["private"]
        mgmt = PortfolioMgmt(api_url, auth=CoinbaseAuth(API_KEY, API_SECRET))
        if hasattr(args, 'p_currency'):
            currency = args.p_currency
            print(f"Sell price : {mgmt.price(currency)} €")
            print(f"Buy price : {mgmt.price(currency, mode='buy')} €")
        elif hasattr(args, "w_currency"):
            print(mgmt.wallet(args.w_currency))
        elif hasattr(args, "b_currency"):
            balance = mgmt.wallet(args.b_currency).balance.count
            sell_price = float(mgmt.price(args.b_currency))
            total = balance*sell_price
            print(f"{round(total, 2)} €")
        else:
            parser.print_help()
    except KeyError:
        print("Incorrect configurations")
        exit(1)
