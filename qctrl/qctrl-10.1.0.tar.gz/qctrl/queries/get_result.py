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
from typing import Union

from gql import gql
from graphql import GraphQLType

from qctrl.builders.custom_environment import QctrlGraphQLEnvironment

from .base import BaseQuery

LOGGER = logging.getLogger(__name__)


class GetResultQuery(BaseQuery):
    """This class is used to retrieve the results of a previously run `function`.
    If the function is still running it will wait until it's finished
    before returning the results."""

    def __call__(
        self, env: QctrlGraphQLEnvironment, action_id: Union[str, int]
    ):  # pylint:disable=arguments-differ
        get_mutation_name_query = gql(
            """
            query getMutationName($modelId: String!) {
                action(modelId: $modelId) {
                    action {
                        ... on CoreAction {
                            mutationName
                        }
                    }
                    errors {
                        message
                    }
                }
            }
        """
        )

        response = self._execute(get_mutation_name_query, {"modelId": str(action_id)})
        self._handle_errors(get_mutation_name_query, response)

        mutation_name = response["action"]["action"].get("mutationName")
        field_type = self._get_mutation_result_type(mutation_name)

        refresh_query = env.build_refresh_query(field_type, action_id)
        response = self._execute(refresh_query)
        self._handle_errors(refresh_query, response)

        result = env.load_data(field_type, response["coreAction"]["coreAction"])
        env.wait_for_completion(field_type, result, refresh_query)
        return result

    def _get_mutation_result_type(self, mutation_name: str) -> GraphQLType:
        """Returns the GraphQLType for the given mutation.

        Parameters
        ----------
        mutation_name : str
            The name of the mutation field in the schema.


        Returns
        -------
        GraphQLType
            Result type of the mutation

        Raises
        ------
        KeyError
            invalid mutation name.
        """
        mutation_type = self._client.schema.get_type("Mutation")
        assert mutation_type

        try:
            mutation_field = mutation_type.fields[mutation_name]
        except KeyError as error:
            raise KeyError(f"unknown mutation: {mutation_name}") from error

        return mutation_field.type
