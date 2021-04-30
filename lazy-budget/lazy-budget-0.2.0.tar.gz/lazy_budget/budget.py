import csv
import os
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from functools import partial
from math import ceil
from typing import ClassVar, Generator, List, Union

import yaml

from lazy_budget.money_provider import (
    DEFAULT_CURRENCY,
    Currency,
    Money,
    get_zero,
    money_mean,
    parse_money,
)


@dataclass
class FinancialOperation:
    money_value: Money
    description: str = ""
    dttm: datetime = field(default_factory=datetime.now())

    CSV_FIELD_NAMES: ClassVar[List[str]] = ["money_value", "description", "dttm"]

    @property
    def currency(self) -> Currency:
        return self.money_value.currency

    @classmethod
    def from_row(cls, row, default_currency: Currency = DEFAULT_CURRENCY):
        money_value = parse_money(row["money_value"], default_currency)
        return cls(
            money_value=money_value,
            description=row["description"],
            dttm=datetime.fromisoformat(row["dttm"]),
        )

    @classmethod
    def from_file(
        cls, filename: os.PathLike, default_currency: Currency = DEFAULT_CURRENCY
    ) -> None:
        with open(filename, "r") as fp:
            reader = csv.DictReader(fp, fieldnames=cls.CSV_FIELD_NAMES)
            yield from map(
                partial(cls.from_row, default_currency=default_currency), reader
            )

    def save(self, filename: os.PathLike) -> None:
        mode = "a" if os.path.isfile(filename) else "w"
        with open(filename, mode) as fp:
            writer = csv.DictWriter(fp, fieldnames=self.CSV_FIELD_NAMES)
            writer.writerow(
                {
                    "money_value": self.money_value.amount,
                    "description": self.description,
                    "dttm": self.dttm,
                }
            )


@dataclass
class Budget:
    total: Money
    keep: Money
    start: date
    end: date
    currency: Currency = Currency.USD
    today: date = None

    def __post_init__(self):
        if not self.today:
            self.today = date.today()

    def __contains__(self, item: Union[date, datetime]) -> bool:
        if isinstance(item, datetime):
            item = item.date()
        elif not isinstance(item, date):
            raise TypeError(
                f"cannot determine if an instance of class {item.__class__.__name__} is within a budget"
            )

        return self.start <= item <= self.end

    def __iter__(self) -> Generator[date, None, None]:
        """
        Returns an Iterable of dates within this budget.
        """
        return (
            self.end - timedelta(days=num_days)
            for num_days in range(self.total_days - 1, -1, -1)
        )

    @property
    def zero(self):
        return get_zero(self.currency)

    @property
    def past_days(self) -> Generator[date, None, None]:
        return filter(lambda x: x <= self.today, iter(self))

    @property
    def is_ongoing(self) -> bool:
        return self.today in self

    @property
    def total_days(self) -> int:
        return (self.end - self.start + timedelta(days=1)).days

    @property
    def days_left(self) -> int:
        return (self.end - self.today).days

    @property
    def available_per_day(self) -> Money:
        return (self.total - self.keep) / self.total_days

    def get_spent_by_day(self, operations: List[FinancialOperation]) -> Money:
        result = defaultdict(lambda: self.zero)
        days = list(self.past_days)
        for operation in filter(lambda op: op.dttm.date() in days, operations):
            result[operation.dttm.date()] += operation.money_value

        return result

    def get_avg_spent_per_day(self, operations: List[FinancialOperation]) -> Money:
        spent_by_day = self.get_spent_by_day(operations)
        return -money_mean((spent_by_day[day] for day in self.past_days), self.currency)

    def get_can_spend_today(self, operations: List[FinancialOperation]) -> Money:
        progress = self.zero
        spent_by_day = self.get_spent_by_day(operations)
        for day in self.past_days:
            progress += self.available_per_day + spent_by_day[day]

        return progress

    def get_days_until_can_spend(
        self, can_spend_today: Money, available_per_day: Money
    ) -> int:
        if can_spend_today >= self.zero:
            return 0

        return int(ceil(-can_spend_today / available_per_day))

    def get_spent_today(self, operations: List[FinancialOperation]) -> Money:
        spent_by_day = self.get_spent_by_day(operations)
        spent_today = spent_by_day[self.today]
        if spent_today < self.zero:
            return -spent_today

        return self.zero

    @classmethod
    def from_file(
        cls, filename: os.PathLike, default_currency: Currency = DEFAULT_CURRENCY
    ) -> None:
        with open(filename, "r") as fp:
            data = yaml.safe_load(fp)

        currency_name = data.get("currency")
        currency = getattr(Currency, currency_name.upper(), default_currency)
        return cls(
            total=parse_money(data["total"], default_currency=currency),
            keep=parse_money(data["keep"], default_currency=currency),
            start=data["start"],
            end=data["end"],
            currency=currency,
        )

    def filter(self, operations: List[FinancialOperation]) -> List[FinancialOperation]:
        return list(
            filter(
                lambda op: op.dttm in self and op.currency == self.currency, operations
            )
        )


@dataclass
class BudgetStats:
    today: date
    total_days: int
    days_left: int
    available_per_day: Money
    can_spend_today: Money
    avg_spent_per_day: Money
    currently_keeping: Money
    spent_today: Money
    currency: Currency
    days_until_can_spend: int = 0

    @classmethod
    def get_stats(
        cls, budget: Budget, operations: List[FinancialOperation]
    ) -> "BudgetStats":
        if not budget.is_ongoing:
            raise ValueError("there can be no stats for a finished budget")

        operations = budget.filter(operations)
        can_spend_today = budget.get_can_spend_today(operations)
        available_per_day = budget.available_per_day
        return cls(
            today=budget.today,
            total_days=budget.total_days,
            days_left=budget.days_left,
            available_per_day=available_per_day,
            can_spend_today=can_spend_today,
            days_until_can_spend=budget.get_days_until_can_spend(
                can_spend_today, available_per_day
            ),
            avg_spent_per_day=budget.get_avg_spent_per_day(operations),
            currently_keeping=budget.keep + can_spend_today,
            spent_today=budget.get_spent_today(operations),
            currency=budget.currency,
        )
