from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import datetime
from os import PathLike

import yaml

from lazy_budget.budget import Budget, BudgetStats, FinancialOperation
from lazy_budget.constants import (
    BUDGET_FILE,
    CONFIG_FILE_PATH,
    DEFAULT_LOCALE,
    HISTORY_FILE,
)
from lazy_budget.display import BasicStatsDisplay
from lazy_budget.money_provider import DEFAULT_CURRENCY, parse_money, str_to_currency


def add_new_operation(args):
    budget = Budget.from_file(args.budget_file, args.currency)
    op = FinancialOperation(
        money_value=parse_money(args.value, budget.currency),
        description=args.description,
        dttm=datetime.fromisoformat(args.dttm),
    )
    op.save(args.history_file)


def list_stats(args):
    budget = Budget.from_file(args.budget_file, args.currency)
    ops = FinancialOperation.from_file(args.history_file, args.currency)
    stats = BudgetStats.get_stats(budget, ops)
    display = BasicStatsDisplay(stats, locale=args.locale)
    print(display)


@dataclass
class CLIConfig:
    history_file: PathLike = HISTORY_FILE
    budget_file: PathLike = BUDGET_FILE
    locale: str = DEFAULT_LOCALE
    currency: str = DEFAULT_CURRENCY.name

    def get_args(self, argv=None):
        parser = ArgumentParser()
        parser.add_argument(
            "-f",
            "--history-file",
            help=f"history file to use (default is {self.history_file})",
            default=self.history_file,
        )
        parser.add_argument(
            "-c",
            "--budget-file",
            help=f"budget file to use (default is {self.budget_file})",
            default=self.budget_file,
        )
        parser.add_argument(
            "-L",
            "--locale",
            help=f"locale to use (default is {self.locale})",
            default=self.locale,
        )
        parser.add_argument(
            "-C",
            "--currency",
            help=f"default currency to use in uncertain situations (default is {self.currency})",
            default=self.currency,
            type=str_to_currency,
        )

        parser.set_defaults(action_func=lambda args: None)
        subparsers = parser.add_subparsers(
            help="whether you want to add an expense or see statistics"
        )

        parser_add = subparsers.add_parser(
            "add", aliases=["a", "new", "n"], help="add a new financial operation"
        )
        parser_add.set_defaults(action_func=add_new_operation)
        parser_add.add_argument("value")
        parser_add.add_argument("description")
        parser_add.add_argument("dttm", nargs="?", default=datetime.now().isoformat())

        parser_today = subparsers.add_parser(
            "ls",
            aliases=["now", "today", "list", "stats", "s", "get"],
            help="list statistics",
        )
        parser_today.set_defaults(action_func=list_stats)

        return parser.parse_args(argv)

    @classmethod
    def from_file(cls, filename: PathLike = CONFIG_FILE_PATH) -> "CLIConfig":
        try:
            with open(filename, "r") as fp:
                data = yaml.safe_load(fp)
        except IOError:
            return cls()

        return cls(**data)
