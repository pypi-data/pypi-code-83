import re
from typing import Any, Dict, Iterable, List, Tuple, Union

from .helpers import (
    replace_regex_groups_with_non_capturing_groups,
    string_replace_with_dict,
    substitute_brackets,
    substitute_quotes,
)


class SqlParser:
    clauses = [
        "SELECT",
        "FROM",
        "LEFT (?:OUTER )?JOIN",
        "RIGHT (?:OUTER )?JOIN",
        "FULL (?:OUTER )?JOIN",
        "(?:INNER )?JOIN",
        "WHERE",
        "QUALIFY",
        "GROUP BY",
        "ORDER BY",
        "HAVING",
    ]

    @classmethod
    def _build_clause_regex(cls) -> str:
        """Builds main regex to capture all clauses, as identified above."""
        reg_base = (r"(?:^|\s+){}\s+|" * len(cls.clauses))[:-1]
        reg = reg_base.format(*cls.clauses)
        return reg

    def __init__(self):
        pass

    def _resolve_with_clauses(self, document: str) -> str:
        reg = r"with ([\w_]+) as (\([^\)]*\))"
        non_capturing_reg = replace_regex_groups_with_non_capturing_groups(reg)

        with_as_matches = [
            self._clean_list(with_as) for with_as in re.findall(reg, document)
        ]
        with_as_mapping = {
            rf"(?:^|\s+){with_}(?:$|\s+)": f" {as_} " for with_, as_ in with_as_matches
        }

        document = self._clean_string(" ".join(re.split(non_capturing_reg, document)))
        document = string_replace_with_dict(document, with_as_mapping)

        return document

    @substitute_quotes
    def _clean_document(self, document: str) -> str:
        document = re.sub(r"(?:--|#).*", "", document)  # remove comments
        document = self._clean_string(document)
        document = re.sub(r"\/\*.*\*\/", "", document)  # remove comments
        document = self._resolve_with_clauses(document)
        return document

    def _clean_string(self, string: str) -> str:
        string = re.sub(r"\s+", " ", string)  # standardize whitespace
        string = string.strip().lower()  # strip and lowercase
        return string

    def _clean_list(self, lst: Iterable[str]) -> List[str]:
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

    def _split_source_value(self, value: str) -> Dict[str, str]:
        """Value splitting for sources (origin FROM / JOIN)"""
        split_on_whitespace = self._clean_split(value)

        if len(split_on_whitespace) > 1:
            split_on_whitespace.insert(1, "as")

        value = " ".join(split_on_whitespace)
        return self._split_value_into_content_and_alias(value)

    def _split_join_on_value(self, value: str) -> Dict[str, List[str]]:
        """Value splitting join on specifications"""
        return {"on": self._clean_split(value, r"\s+and\s+")}

    def _split_join_value(self, value: str) -> Dict[str, Union[str, List[str]]]:
        """Value splitting for joins"""
        source, join_on = self._clean_split(value, r"\s+on\s+", maxsplit=1)

        return {
            **self._split_source_value(source),
            **self._split_join_on_value(join_on),
        }

    def _split_condition_value(self, value: str) -> List[str]:
        """Value splitting for conditions (WHERE / QUALIFY / HAVING)"""
        return self._clean_split(value, r"\s+and\s+")

    def _split_enumeration_value(
        self, clause: str, value: str
    ) -> Union[List[str], List[Dict[str, str]]]:
        """Value splitting for enumerations (SELECT, GROUP BY, ORDER BY)"""
        statements = self._clean_split(value, ",")
        if clause == "select":
            return list(map(self._split_value_into_content_and_alias, statements))
        return statements

    def _split_value(self, clause: str, value: str) -> Any:
        """Function for splitting values based on right clause"""
        return (
            self._split_source_value(value)
            if clause == "from"
            else self._split_join_value(value)
            if "join" in clause
            else self._split_condition_value(value)
            if clause in ("where", "qualify", "having")
            else self._split_enumeration_value(clause, value)
            if clause in ("select", "group by", "order by")
            else value
        )

    def _standardize_clauses(self, clauses: List[str]) -> List[str]:
        # remove outer keyword (LEFT/RIGHT/FULL OUTER JOIN)
        clauses = [re.sub(" outer ", " ", clause) for clause in clauses]
        # map join to inner join
        clauses = ["inner join" if clause == "join" else clause for clause in clauses]

        return clauses

    @substitute_brackets
    def _split_clauses_and_values(self, query: str) -> Tuple[List[str], List[str]]:
        """Starting point for parsing. Split into clauses and values."""
        reg = self._build_clause_regex()

        clauses = self._clean_list(re.findall(reg, query, flags=re.I))
        values = self._clean_list(re.split(reg, query, flags=re.I))

        return self._standardize_clauses(clauses), values

    def parse(self, document: str) -> Union[list, dict]:
        """Callable for user."""
        return self._parse(self._clean_document(document))

    def _parse(self, document: str) -> Union[list, dict]:
        """Test for unions -> leads to different parsing layout."""
        union_split = self._clean_split(document, r"UNION (?:ALL)?")

        if len(union_split) == 1:
            return self._parse_query(document)
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
                        self._clean_string(split_value["content"])
                        .lstrip("(")
                        .rstrip(")")
                    )
                    # Continue parsing inner SQL
                    split_value["content"] = self._parse(without_brackets)

            # Re-join clause and value
            combinations[clause] = split_value

        return combinations
