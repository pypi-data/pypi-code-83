import re
from typing import Any, Dict, List, Tuple, Union

from .helpers import substitute_brackets


class SqlParser:
    clauses = [
        "SELECT",
        "FROM",
        "LEFT JOIN",
        "LEFT OUTER JOIN",
        "RIGHT JOIN",
        "RIGHT OUTER JOIN",
        "FULL JOIN",
        "FULL OUTER JOIN",
        "INNER JOIN",
        "WHERE",
        "QUALIFY",
    ]

    @classmethod
    def _build_clause_regex(cls) -> str:
        """Builds main regex to capture all clauses, as identified above."""
        reg_base = (r"(?:^|\s+){}\s+|" * len(cls.clauses))[:-1]
        reg = reg_base.format(*cls.clauses)
        return reg

    def __init__(self):
        pass

    def _clean_string(self, string: str) -> str:
        string = re.sub(r"#.*", "", string)  # remove comments
        string = re.sub(r"\s+", " ", string)  # standardize whitespace
        string = re.sub(r"\/\*.*\*\/", "", string)  # remove comments
        string = string.strip().lower()
        return string

    def _clean_list(self, lst: List[str]) -> List[str]:
        cleaned = filter(lambda item: item, lst)  # remove empty values
        return list(map(self._clean_string, cleaned))

    @substitute_brackets
    def _clean_split(
        self, string: str, pattern: str = r"\s+", maxsplit: int = 0
    ) -> List[str]:
        return self._clean_list(re.split(pattern, string, maxsplit, flags=re.I))

    def _split_value_into_content_and_alias(self, value: str) -> Dict[str, str]:
        """Function for aliasing (used in source clauses and SELECT items)"""
        keys = ["content", "alias"]
        return dict(zip(keys, self._clean_split(value, r"\s+as\s+")))

    def _split_select_value(self, value: str) -> List[Dict[str, str]]:
        """SELECT statement value splitting"""
        select_statements = self._clean_split(value, ",")
        return list(map(self._split_value_into_content_and_alias, select_statements))

    def _split_source_value(self, value: str) -> Dict[str, str]:
        """Value splitting for sources (FROM / JOIN)"""
        split_on_whitespace = self._clean_split(value)

        if len(split_on_whitespace) == 2:
            split_on_whitespace.insert(1, "as")

        value = " ".join(split_on_whitespace)
        return self._split_value_into_content_and_alias(value)

    def _split_join_on(self, value: str) -> Dict[str, List[str]]:
        """JOIN statement value splitting"""
        return {"on": self._clean_split(value, r"\s+and\s+")}

    def _split_join_value(self, value: str) -> Dict[str, Union[str, List[str]]]:
        """Join on value splitting"""
        source, join_on = self._clean_split(value, r"\s+on\s+", maxsplit=1)

        return {**self._split_source_value(source), **self._split_join_on(join_on)}

    def _split_condition_value(self, value: str) -> List[str]:
        """Condition statement value splitting (WHERE / QUALIFY)"""
        return self._clean_split(value, r"\s+and\s+")

    def _split_value(self, clause: str, value: str) -> Any:
        """Function for splitting values based on right clause"""
        return (
            self._split_select_value(value)
            if clause == "select"
            else self._split_source_value(value)
            if clause == "from"
            else self._split_join_value(value)
            if "join" in clause
            else self._split_condition_value(value)
            if clause in ("where", "qualify")
            else value
        )

    @substitute_brackets
    def _split_clauses_and_values(self, query: str) -> Tuple[List[str], List[str]]:
        """Starting point for parsing. Split into clauses and values."""
        reg = self._build_clause_regex()

        clauses = self._clean_list(re.findall(reg, query, flags=re.I))
        values = self._clean_list(re.split(reg, query, flags=re.I))

        return clauses, values

    def parse(self, input_string: str) -> Union[list, dict]:
        """Callable for user."""
        return self._parse(self._clean_string(input_string))

    def _parse(self, input_string: str) -> Union[list, dict]:
        """Test for unions -> leads to different parsing layout."""
        union_split = self._clean_split(input_string, r"UNION\s+(?:ALL)?")

        if len(union_split) == 1:
            return self._parse_query(input_string)
        else:
            return [self._parse_query(query) for query in union_split]

    def _parse_query(self, query: str) -> dict:
        """Parse a complete query (assume starts with SELECT)"""
        clauses, values = self._split_clauses_and_values(query)

        # If clause is not the first argument, omit what precedes
        # first encountered clause
        values = values if len(clauses) == len(values) else values[1:]

        combinations = {}
        for clause, value in zip(clauses, values):
            split_value = self._split_value(clause, value)

            # Detect inner SQL
            if "join" in clause or clause == "from":
                if "select" in split_value["content"]:
                    without_brackets = (
                        split_value["content"].strip().lstrip("(").rstrip(")")
                    )
                    # Continue parsing inner SQL
                    split_value["content"] = self._parse(without_brackets)

            # Re-join clause and value
            combinations[clause] = split_value

        return combinations
