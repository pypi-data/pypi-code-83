# Copyright 2020 Q-CTRL Pty Ltd & Q-CTRL Inc. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
# pylint:disable=missing-module-docstring
import logging
from abc import ABC
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)

from gql import (
    Client,
    gql,
)
from gql.transport.exceptions import TransportQueryError
from graphql import DocumentNode
from qctrlcommons.exceptions import QctrlGqlException

LOGGER = logging.getLogger(__name__)
Query = Union[DocumentNode, str]


class DocumentHelper:
    """Provides extra functionality for DocumentNode objects."""

    def __init__(self, document: DocumentNode):
        self._document = document

    @property
    def query_result_keys(self) -> List[str]:
        """Returns the list of root-level keys for the response
        data that contain the queried data.
        """
        keys = []

        for op_def_node in self._document.definitions:
            for field_node in op_def_node.selection_set.selections:
                if field_node.alias:
                    keys.append(field_node.alias.value)
                else:
                    keys.append(field_node.name.value)

        return keys


class BaseQuery(ABC):
    """Base class for wrapping a GraphQL query with custom
    validation, error handling and result formatting.
    """

    query: Query = None

    def __init__(self, client: Client):
        self._client = client

    def __call__(self, *args, **kwargs):
        """Executes the GraphQL query and returns a formatted
        result.
        """

        variable_values = self._get_variable_values(*args, **kwargs)

        if isinstance(self.query, DocumentNode):
            document = self.query

        elif isinstance(self.query, str):
            document = gql(self.query)

        else:
            raise ValueError(f"invalid query type: {self.query}")

        return self._process(document, variable_values)

    def _process(
        self, document: DocumentNode, variable_values: Optional[Dict[str, Any]] = None
    ):
        """Processes the GraphQL query. Sends the query to the server,
        handles any errors and returns the formatted result.

        Parameters
        ----------
        document: DocumentNode
            GraphQL query to be executed.
        variable_values: Optional[Dict[str, Any]]
            required variable values for the document.

        Returns
        -------
        Any
            the formatted response provided by the subclass.
        """
        response = self._execute(document, variable_values)
        LOGGER.debug("response: %s", response)
        self._handle_errors(document, response)
        return self._format_response(response)

    def _get_variable_values(  # pylint:disable=no-self-use
        self, *args, **kwargs  # pylint:disable=unused-argument
    ) -> Dict[str, Any]:
        """Converts the args and kwargs provided when calling the
        object to the variable values dict required when executing
        the document. Performs any necessary validation. To be
        overridden by the subclass. By default, an empty dictionary
        is returned.

        Returns
        -------
        Dict[str, Any]
            the variables required to execute the document.

        Raises
        ------
        QctrlGqlException
            any validation errors.
        """
        return {}

    def _execute(
        self, document: DocumentNode, variable_values: Optional[Dict[str, Any]] = None
    ) -> dict:
        """Sends a GraphQL request to the server using the document
        and variable values.

        Parameters
        ----------
        document: DocumentNode
            GraphQL query to be executed.
        variable_values: Optional[Dict[str, Any]]
            required variable values for the document.

        Returns
        -------
        dict
            the response data from the server.

        Raises
        ------
        QctrlGqlException
            any transport errors when accessing the server.
        """
        try:
            return self._client.execute(document, variable_values=variable_values)
        except TransportQueryError as exc:
            raise QctrlGqlException(exc.errors) from exc

    def _format_response(self, response: dict) -> dict:  # pylint:disable=no-self-use
        """Formats the query response into the expected format. Can
        be overridden by the subclass. By default, the query response
        is returned unaltered.

        Parameters
        ----------
        response: dict
            query response data returned from server.

        Returns
        -------
        dict
            by default, returns the response.

        Raises
        ------
        QctrlGqlException
            any expected error.
        """
        return response

    @staticmethod
    def _handle_errors(document: DocumentNode, response: dict):
        """Performs error handling on the GraphQL response.

        Parameters
        ----------
        document: DocumentNode
            GraphQL document sent to server
        response: dict
            corresponding response data for document

        Raises
        ------
        QctrlGqlException
            any returned errors.
        """

        # check root level errors
        root_errors = response.get("errors")

        if root_errors:
            raise QctrlGqlException(root_errors, format_to_snake=True)

        # check query level errors
        for key in DocumentHelper(document).query_result_keys:
            query_errors = response.get(key, {}).get("errors")

            if query_errors:
                raise QctrlGqlException(response[key]["errors"], format_to_snake=True)
