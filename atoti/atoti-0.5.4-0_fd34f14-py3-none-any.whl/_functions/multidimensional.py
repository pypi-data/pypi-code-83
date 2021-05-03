from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Collection, Mapping, Optional, Union

from typing_extensions import Literal

from .._measures.generic_measure import GenericMeasure
from .._measures.utils import get_measure_name
from .._vendor.atotipy4j.protocol import JAVA_MAX_INT
from ..hierarchy import Hierarchy
from ..level import Level
from ..measure import Measure, MeasureLike

if TYPE_CHECKING:
    from typing import List, Tuple

    from .._java_api import JavaApi
    from ..cube import Cube


@dataclass(eq=False)
class ParentValue(Measure):
    """The value of the measure for the parent."""

    _underlying_measure: Union[Measure, str]
    _hierarchies: Collection[Hierarchy]
    _total_value: Optional[MeasureLike]
    _apply_filters: bool
    _degrees: Mapping[Hierarchy, int]

    def _do_distil(
        self, java_api: JavaApi, cube: Cube, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = (
            self._underlying_measure
            if isinstance(self._underlying_measure, str)
            else get_measure_name(java_api, self._underlying_measure, cube)
        )
        total_measure_name = (
            self._total_value._distil(java_api, cube, None)
            if isinstance(self._total_value, Measure)
            else None
        )
        total_literal = self._total_value if total_measure_name is None else None

        distilled_name = java_api.create_measure(
            cube,
            measure_name,
            "PARENT_VALUE",
            underlying_name,
            {
                hierarchy: self._degrees.get(hierarchy, 1)
                for hierarchy in self._hierarchies
            },
            total_measure_name,
            total_literal,
            self._apply_filters,
        )
        return distilled_name


def parent_value(
    measure: Union[Measure, str],
    on: Union[Hierarchy, Collection[Hierarchy]],
    *,
    apply_filters: bool = False,
    total_value: Optional[MeasureLike] = None,
    degrees: Optional[Mapping[Hierarchy, int]] = None,
) -> Measure:
    """Return a measure equal to the passed measure at the parent member on the given hierarchies.

    Args:
        measure: The measure to take the parent value of.
        on: Hierarchy or hierarchies to drill up to take the parent value.
        apply_filters: Whether to apply the query filters when computing the value at the parent member.
        total_value: The value to take when the drill up went above the top level of the hierarchy.
        degrees: The number of levels to go up to take the value on each given hierarchy.
            If a hierarchy is not specified, a degree of ``1`` is used.

    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Year", "Month", "Day", "Quantity", "Other"],
        ...     data=[
        ...         (2019, 7, 1, 15.0, 245.0),
        ...         (2019, 7, 2, 20.0, 505.0),
        ...         (2019, 6, 1, 25.0, 115.0),
        ...         (2019, 6, 2, 15.0, 135.0),
        ...         (2018, 7, 1, 5.0, 55.0),
        ...         (2018, 7, 2, 10.0, 145.0),
        ...         (2018, 6, 1, 15.0, 145.0),
        ...         (2018, 6, 2, 5.0, 155.0),
        ...     ],
        ... )
        >>> store = session.read_pandas(
        ...     df,
        ...     store_name="Parent Value",
        ...     hierarchized_columns=["Year", "Month", "Day"],
        ... )
        >>> cube = session.create_cube(store)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> del h["Year"]
        >>> del h["Month"]
        >>> del h["Day"]
        >>> h["Date"] = [store["Year"], store["Month"], store["Day"]]
        >>> m["Degree 1"] = tt.parent_value(m["Quantity.SUM"], h["Date"])
        >>> m["Degree 2"] = tt.parent_value(
        ...     m["Quantity.SUM"], h["Date"], degrees={h["Date"]: 2}
        ... )
        >>> m["Degree 2 with Quantity total"] = tt.parent_value(
        ...     m["Quantity.SUM"],
        ...     h["Date"],
        ...     degrees={h["Date"]: 2},
        ...     total_value=m["Quantity.SUM"],
        ... )
        >>> m["Degree 2 with Other total"] = tt.parent_value(
        ...     m["Quantity.SUM"],
        ...     h["Date"],
        ...     degrees={h["Date"]: 2},
        ...     total_value=m["Other.SUM"],
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Other.SUM"],
        ...     m["Degree 1"],
        ...     m["Degree 2"],
        ...     m["Degree 2 with Quantity total"],
        ...     m["Degree 2 with Other total"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                        Quantity.SUM Other.SUM Degree 1 Degree 2 Degree 2 with Quantity total Degree 2 with Other total
        Year  Month Day
        Total                 110.00  1,500.00                                         110.00                  1,500.00
        2018                   35.00    500.00   110.00                                110.00                  1,500.00
              6                20.00    300.00    35.00   110.00                       110.00                    110.00
                    1          15.00    145.00    20.00    35.00                        35.00                     35.00
                    2           5.00    155.00    20.00    35.00                        35.00                     35.00
              7                15.00    200.00    35.00   110.00                       110.00                    110.00
                    1           5.00     55.00    15.00    35.00                        35.00                     35.00
                    2          10.00    145.00    15.00    35.00                        35.00                     35.00
        2019                   75.00  1,000.00   110.00                                110.00                  1,500.00
              6                40.00    250.00    75.00   110.00                       110.00                    110.00
                    1          25.00    115.00    40.00    75.00                        75.00                     75.00
                    2          15.00    135.00    40.00    75.00                        75.00                     75.00
              7                35.00    750.00    75.00   110.00                       110.00                    110.00
                    1          15.00    245.00    35.00    75.00                        75.00                     75.00
                    2          20.00    505.00    35.00    75.00                        75.00                     75.00
        >>> h["Date"].slicing = True
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Other.SUM"],
        ...     m["Degree 1"],
        ...     m["Degree 2"],
        ...     m["Degree 2 with Quantity total"],
        ...     m["Degree 2 with Other total"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                       Quantity.SUM Other.SUM Degree 1 Degree 2 Degree 2 with Quantity total Degree 2 with Other total
        Year Month Day
        2018 6     1          15.00    145.00    20.00    35.00                        35.00                     35.00
                   2           5.00    155.00    20.00    35.00                        35.00                     35.00
             7     1           5.00     55.00    15.00    35.00                        35.00                     35.00
                   2          10.00    145.00    15.00    35.00                        35.00                     35.00
        2019 6     1          25.00    115.00    40.00    75.00                        75.00                     75.00
                   2          15.00    135.00    40.00    75.00                        75.00                     75.00
             7     1          15.00    245.00    35.00    75.00                        75.00                     75.00
                   2          20.00    505.00    35.00    75.00                        75.00                     75.00

    See Also:
        :func:`atoti.total` to take the value at the top level member on each given hierarchy.

    """
    return ParentValue(
        measure,
        on if isinstance(on, Collection) else [on],
        total_value,
        apply_filters,
        degrees if degrees is not None else {},
    )


def total(measure: Measure, *hierarchies: Hierarchy) -> Measure:
    """Return a measure equal to the passed measure at the top level member on each given hierarchy.

    It ignores the filters on this hierarchy.

    If the hierarchy is not slicing, total is equal to the value for all the members.
    If the hierarchy is slicing, total is equal to the value on the first level.

    Args:
        measure: The measure to take the total of.
        hierarchies: The hierarchies on which to find the top-level member.


    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Year", "Month", "Day", "Price"],
        ...     data=[
        ...         (2019, 7, 1, 15.0),
        ...         (2019, 7, 2, 20.0),
        ...         (2019, 6, 1, 25.0),
        ...         (2019, 6, 2, 15.0),
        ...         (2018, 7, 1, 5.0),
        ...         (2018, 7, 2, 10.0),
        ...         (2018, 6, 1, 15.0),
        ...         (2018, 6, 2, 5.0),
        ...     ],
        ... )
        >>> store = session.read_pandas(
        ...     df,
        ...     store_name="Total",
        ...     hierarchized_columns=["Year", "Month", "Day"],
        ... )
        >>> cube = session.create_cube(store)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> del h["Year"]
        >>> del h["Month"]
        >>> del h["Day"]
        >>> h["Date"] = [store["Year"], store["Month"], store["Day"]]
        >>> m["Total(Price)"] = tt.total(m["Price.SUM"], h["Date"])
        >>> cube.query(
        ...     m["Price.SUM"],
        ...     m["Total(Price)"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                        Price.SUM Total(Price)
        Year  Month Day
        Total              110.00       110.00
        2018                35.00       110.00
              6             20.00       110.00
                    1       15.00       110.00
                    2        5.00       110.00
              7             15.00       110.00
                    1        5.00       110.00
                    2       10.00       110.00
        2019                75.00       110.00
              6             40.00       110.00
                    1       25.00       110.00
                    2       15.00       110.00
              7             35.00       110.00
                    1       15.00       110.00
                    2       20.00       110.00
        >>> h["Date"].slicing = True
        >>> cube.query(
        ...     m["Price.SUM"],
        ...     m["Total(Price)"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                       Price.SUM Total(Price)
        Year Month Day
        2018 6     1       15.00        35.00
                   2        5.00        35.00
             7     1        5.00        35.00
                   2       10.00        35.00
        2019 6     1       25.00        75.00
                   2       15.00        75.00
             7     1       15.00        75.00
                   2       20.00        75.00

    """
    return ParentValue(
        measure,
        hierarchies,
        measure,
        False,
        {hierarchy: JAVA_MAX_INT for hierarchy in hierarchies},
    )


def shift(measure: Measure, on: Level, *, offset: int = 1) -> Measure:
    """Return a measure equal to the passed measure shifted to another member.

    Args:
        measure: The measure to shift.
        on: The level to shift on.
        offset: The amount of members to shift by.

    """
    return GenericMeasure("LEAD_LAG", measure, on._hierarchy, offset)


@dataclass(eq=False)
class FirstLast(Measure):
    """Shift the value."""

    _underlying_measure: Measure
    _level: Level
    _mode: Literal["FIRST", "LAST"]

    def _do_distil(
        self, java_api: JavaApi, cube: Cube, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = get_measure_name(java_api, self._underlying_measure, cube)
        distilled_name = java_api.create_measure(
            cube,
            measure_name,
            "FIRST_LAST",
            underlying_name,
            self._level,
            self._mode,
        )
        return distilled_name


def _first(measure: Measure, on: Level) -> Measure:
    """Return a measure equal to the first value of the passed measure on the level.

    Example:
        Measure definition::

            m["Turnover first day"] = atoti.first(m["Turnover"], on=l["Date"])

        Considering a single-level hierarchy ``Date``:

        +------------+----------+--------------------+
        |    Date    | Turnover | Turnover first day |
        +============+==========+====================+
        | 2020-01-01 |      100 |                100 |
        +------------+----------+--------------------+
        | 2020-01-02 |      500 |                100 |
        +------------+----------+--------------------+
        | 2020-01-03 |      200 |                100 |
        +------------+----------+--------------------+
        | 2020-01-04 |      400 |                100 |
        +------------+----------+--------------------+
        | 2020-01-05 |      300 |                100 |
        +------------+----------+--------------------+
        | TOTAL      |     1500 |                100 |
        +------------+----------+--------------------+

    Args:
        measure: The measure to shift.
        on: The level to shift on.

    """
    return FirstLast(measure, on, "FIRST")


def _last(measure: Measure, on: Level) -> Measure:
    """Return a measure equal to the last value of the passed measure on the level.

    Example:
        Measure definition::

            m["Turnover last day"] = atoti.last(m["Turnover"], on=l["Date"])

        Considering a single-level hierarchy ``Date``:

        +------------+----------+-------------------+
        |    Date    | Turnover | Turnover last day |
        +============+==========+===================+
        | 2020-01-01 |      100 |               300 |
        +------------+----------+-------------------+
        | 2020-01-02 |      500 |               300 |
        +------------+----------+-------------------+
        | 2020-01-03 |      200 |               300 |
        +------------+----------+-------------------+
        | 2020-01-04 |      400 |               300 |
        +------------+----------+-------------------+
        | 2020-01-05 |      300 |               300 |
        +------------+----------+-------------------+
        | TOTAL      |     1500 |               300 |
        +------------+----------+-------------------+

    Args:
        measure: The measure to shift.
        on: The level to shift on.

    """
    return FirstLast(measure, on, "LAST")


@dataclass(eq=False)
class DateShift(Measure):
    """Shift the value."""

    _underlying_measure: Measure
    _hierarchy_name: str
    _shift: str
    _method: str

    def _do_distil(
        self, java_api: JavaApi, cube: Cube, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = get_measure_name(java_api, self._underlying_measure, cube)
        levels = cube.hierarchies[self._hierarchy_name].levels
        level = list(levels.values())[-1]
        distilled_name = java_api.create_measure(
            cube,
            measure_name,
            "DATE_SHIFT",
            underlying_name,
            level,
            self._shift,
            self._method,
        )
        return distilled_name


_DateShiftMethod = Literal[  # pylint: disable=invalid-name
    "exact", "previous", "following", "interpolate"
]


def date_shift(  # pylint: disable=invalid-name
    measure: Measure,
    on: Hierarchy,
    offset: str,
    *,
    method: _DateShiftMethod = "exact",
) -> Measure:
    """Return a measure equal to the passed measure shifted to another date.

    Args:
        measure: The measure to shift.
        on: The hierarchy to shift on.
            Only hierarchies with a single level of type date (or datetime) are supported.
            If one of the member of the hierarchy is ``N/A`` their shifted value will always be ``None``.
        offset: The offset of the form ``xxDxxWxxMxxQxxY`` to shift by.
            Only the ``D``, ``W``, ``M``, ``Q``, and ``Y`` offset aliases are supported.
            Offset aliases have the `same meaning as Pandas' <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.
        method: Determine the value to use when there is no member at the shifted date:

            * ``exact``: ``None``.
            * ``previous``: Value at the previous existing date.
            * ``following``: Value at the following existing date.
            * ``interpolate``: Linear interpolation of the values at the previous and following existing dates:

                Example::

                    m2 = atoti.date_shift("m1", on=h["date"], offset="1M", method="interpolate")

                +------------+----+-------+----------------------------------------------------------------------------+
                |    date    | m1 |   m2  |                         explanation                                        |
                +============+====+=======+============================================================================+
                | 2000-01-05 | 15 | 10.79 | linear interpolation of 2000-02-03's 10 and 2000-03-03's 21 for 2000-02-05 |
                +------------+----+-------+----------------------------------------------------------------------------+
                | 2000-02-03 | 10 |    21 | exact match at 2000-03-03: no need to interpolate                          |
                +------------+----+-------+----------------------------------------------------------------------------+
                | 2000-03-03 | 21 |  9.73 | linear interpolation of 2000-03-03's 21 and 2000-04-05's 9 for 2000-04-03  |
                +------------+----+-------+----------------------------------------------------------------------------+
                | 2000-04-05 |  9 |     ∅ | no record after 2000-04-05: cannot interpolate                             |
                +------------+----+-------+----------------------------------------------------------------------------+

    """
    if len(on.levels) > 1:
        raise ValueError(
            f"Invalid hierarchy {on.name}, "
            "only hierarchies with a single date level are supported."
        )
    return DateShift(measure, on.name, offset, method)


def _unwrap_conditions(
    conditions: Mapping[Level, Any]
) -> Tuple[List[Any], List[Any], List[Any]]:
    """Unwrap a map of conditions.

    Transform a map of conditions into its corresponding list of levels, values, and target
    levels.
    """
    levels = []
    values = []
    target_levels = []
    for level, value in conditions.items():
        levels.append(level)
        if isinstance(value, Level):
            target_levels.append(value)
            values.append(None)
        else:
            target_levels.append(None)
            values.append(value)
    return levels, values, target_levels


def at(measure: Measure, coordinates: Mapping[Level, Any]):
    """Return a measure equal to the passed measure at some other coordinates of the cube.

    Args:
        measure: The measure to take at other coordinates.
        coordinates: A ``{level_to shift_on: value_to_shift_to}`` mapping.
            Values can either be:

            * A literal matching an existing member of the key level::

                # Return the value of Quantity for France on each member of the Country level.
                atoti.at(m["Quantity"], {l["Country"]: "France"})

            * Another level whose current member the key level will be shifted to::

                # Return the value of Quantity for the current member
                # of the Target Country and Target City levels.
                atoti.at(m["Quantity"], {
                    l["Country"]: l["Target Country"],
                    l["City"]: l["Target City"],
                })

              If this other level is not expressed, the shifting will not be done.

    """
    levels, values, target_levels = _unwrap_conditions(coordinates)
    return GenericMeasure("LEVEL_AT", measure, levels, values, target_levels)
