import os
from typing import Any, Dict, List, Union

import requests

from sktmls import MLSENV, MLSRuntimeENV, MLSResponse
from sktmls.config import Config


class Vertex:
    """
    GraphDB의 Vertex 클래스입니다.
    """

    def __init__(self, **kwargs):
        """
        ## Args

        - kwargs
            - id: (str) Vertex 고유 ID
            - label: (str) Vertex 라벨
            - properties: (dict) Vertex property 값들

        ## Returns
        `sktmls.apis.graph_api.Vertex`
        """
        self.id = kwargs.get("id")
        self.label = kwargs.get("label")
        self.properties = kwargs.get("properties")

    def get(self):
        return self.__dict__


class Edge:
    """
    GraphDB의 Edge 클래스입니다.
    """

    def __init__(self, **kwargs):
        """
        ## Args

        - kwargs
            - id: (str) Edge 고유 ID
            - label: (str) Edge 라벨
            - properties: (dict) Edge property 값들

        ## Returns
        `sktmls.apis.graph_api.Edge`
        """
        self.id = kwargs.get("id")
        self.label = kwargs.get("label")
        self.properties = kwargs.get("properties")

    def get(self):
        return self.__dict__


class MLSGraphAPIClient:
    """
    MLS 그래프 API를 호출할 수 있는 클라이언트입니다.

    EDD 환경은 지원하지 않습니다.
    """

    def __init__(
        self,
        env: MLSENV = None,
        runtime_env: MLSRuntimeENV = None,
    ):
        """
        ## Args

        - env: (`sktmls.MLSENV`) 접근할 MLS 환경 (`sktmls.MLSENV.DEV`|`sktmls.MLSENV.STG`|`sktmls.MLSENV.PRD`) (기본값: `sktmls.MLSENV.STG`)
        - runtime_env: (`sktmls.MLSRuntimeENV`) 클라이언트가 실행되는 환경 (`sktmls.MLSRuntimeENV.YE`|`sktmls.MLSRuntimeENV.MMS`|`sktmls.MLSRuntimeENV.LOCAL`) (기본값: `sktmls.MLSRuntimeENV.LOCAL`)

        아래의 환경 변수가 정의된 경우 해당 파라미터를 생략 가능합니다.

        - $MLS_ENV: env
        - $AWS_ENV: env
        - $MLS_RUNTIME_ENV: runtime_env

        ## Returns
        `sktmls.apis.MLSGraphAPIClient`

        ## Example

        ```python
        graph_api_client = MLSGraphAPIClient(env=MLSENV.STG, runtime_env=MLSRuntimeENV.YE)
        ```
        """
        if env:
            assert env in MLSENV.list_items(), "유효하지 않은 MLS 환경입니다."
            self.__env = env
        elif os.environ.get("MLS_ENV"):
            self.__env = MLSENV[os.environ["MLS_ENV"]]
        elif os.environ.get("AWS_ENV"):
            self.__env = MLSENV[os.environ["AWS_ENV"]]
        else:
            self.__env = MLSENV.STG

        if runtime_env:
            assert runtime_env in MLSRuntimeENV.list_items(), "유효하지 않은 런타임 환경입니다."
            self.__runtime_env = runtime_env
        elif os.environ.get("MLS_RUNTINE_ENV"):
            self.__runtime_env = MLSRuntimeENV[os.environ["MLS_RUNTINE_ENV"]]
        else:
            __HOSTNAME = os.environ.get("HOSTNAME", "").lower()
            if __HOSTNAME.startswith("bdp-dmi"):
                self.__runtime_env = MLSRuntimeENV.YE
            elif __HOSTNAME.startswith("vm-skt"):
                self.__runtime_env = MLSRuntimeENV.EDD
            else:
                self.__runtime_env = MLSRuntimeENV.LOCAL

        assert runtime_env != MLSRuntimeENV.EDD, "EDD 환경은 지원하지 않습니다."

        self.config = Config(self.__runtime_env.value)

    def get_env(self) -> MLSENV:
        return self.__env

    def get_runtime_env(self) -> MLSRuntimeENV:
        return self.__runtime_env

    def list_vertices(self, query_params: Dict[str, Union[str, List[str]]] = {}) -> List[Vertex]:
        """
        조건에 해당하는 모든 Vertex의 리스트를 가져옵니다. 100개를 초과하는 경우 100개까지만 가져옵니다.

        ## Args

        - query_params: (optional) (dict) 쿼리 파라미터. 아래 예시 참조 (기본값: {})
            - {property_name}={value}: Vertex.Properties[property_name] == str(value)
            - {property_name}__{operator}
                - eq, gt, gte, lt, lte: Vertex.Properties[property_name] {operator} float(value)
                - bw: {property_name}__bw={value1},{value2}: float(value1) < Vertex.Properties[property_name] < float(value2)

        ## Returns
        list(`sktmls.apis.Vertex`)

        ## Example

        ```python
        # 모든 Vertex 가져오기 (최대 100개로 제한)
        vertices = graph_api_client.list_vertices()

        # `hello` property가 `world`값을 가지며 `latitude` property가 33보다 큰 Vertex를 가져오기
        vertices = graph_api_client.list_vertices(query_params={
            "hello": "world",
            "latitude__gte": 33,
        })
        ```
        """
        params = query_params
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        response = MLSResponse(
            requests.get(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices", params=params)
        ).results

        return [Vertex(**v) for v in response["vertices"]]

    def add_vertex(self, vertex_id: str, label: str, properties: Dict[str, Any] = {}) -> Vertex:
        """
        Vertex를 추가합니다.

        ## Args

        - vertex_id: (str) Vertex의 고유 ID
        - label: (str) Vertex의 라벨
        - properties: (dict) Vertex의 property 키와 값

        ## Returns
        `sktmls.apis.Vertex`

        ## Example

        ```python
        vertex = graph_api_client.add_vertex(
            vertex_id="USER001",
            label="user",
            properties={
                "name": "김유저",
                "age": 30,
            }
        )
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.post(
                f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices",
                params=params,
                json={"id": vertex_id, "label": label, "properties": properties},
            )
        )

        return self.get_vertex(vertex_id)

    def drop_vertices(self, query_params: Dict[str, Union[str, List[str]]] = {}) -> None:
        """
        조건에 해당하는 모든 Vertex를 삭제합니다.

        ## Args

        - query_params: (optional) (dict) 쿼리 파라미터. 아래 예시 참조 (기본값: {})
            - {property_name}={value}: Vertex.Properties[property_name] == str(value)
            - {property_name}__{operator}
                - eq, gt, gte, lt, lte: Vertex.Properties[property_name] {operator} float(value)
                - bw: {property_name}__bw={value1},{value2}: float(value1) < Vertex.Properties[property_name] < float(value2)

        ## Example

        ```python
        # `hello` property가 `world`값을 가지며 `latitude` property가 33보다 큰 Vertex를 삭제하기
        vertices = graph_api_client.delete_vertices(query_params={
            "hello": "world",
            "latitude__gte": 33,
        })
        ```
        """
        params = query_params
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(requests.delete(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices", params=params))

    def get_vertex(self, vertex_id: str) -> Vertex:
        """
        단일 Vertex를 가져옵니다.

        ## Args

        - vertex_id: (str) Vertex의 고유 ID

        ## Returns
        `sktmls.apis.Vertex`

        ## Example

        ```python
        vertex = graph_api_client.get_vertex("USER001")
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        response = MLSResponse(
            requests.get(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices/{vertex_id}", params=params)
        ).results

        return Vertex(**response["vertices"][0])

    def update_vertex(self, vertex_id: str, properties: Dict[str, Any] = {}) -> Vertex:
        """
        단일 Vertex의 property를 업데이트합니다.

        ## Args

        - vertex_id: (str) Vertex의 고유 ID
        - properties: (dict) Vertex의 property 키와 값

        ## Returns
        `sktmls.apis.Vertex`

        ## Example

        ```python
        vertex = graph_api_client.update_vertex(
            vertex_id="USER001",
            properties={
                "age": 35,
            }
        )
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.patch(
                f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices/{vertex_id}",
                params=params,
                json={"properties": properties},
            )
        )

        return self.get_vertex(vertex_id)

    def drop_vertex(self, vertex_id: str) -> None:
        """
        단일 Vertex를 삭제합니다. 연결된 Edge들 역시 삭제됩니다.

        ## Args

        - vertex_id: (str) Vertex의 고유 ID

        ## Example

        ```python
        vertex = graph_api_client.drop_vertex("USER001")
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.delete(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/vertices/{vertex_id}", params=params)
        )

    def list_edges(self, query_params: Dict[str, Union[str, List[str]]] = {}) -> List[Edge]:
        """
        조건에 해당하는 모든 Edge의 리스트를 가져옵니다. 100개를 초과하는 경우 100개까지만 가져옵니다.

        ## Args

        - query_params: (optional) (dict) 쿼리 파라미터. 아래 예시 참조 (기본값: {})
            - {property_name}={value}: Vertex.Properties[property_name] == str(value)
            - {property_name}__{operator}
                - eq, gt, gte, lt, lte: Vertex.Properties[property_name] {operator} float(value)
                - bw: {property_name}__bw={value1},{value2}: float(value1) < Vertex.Properties[property_name] < float(value2)

        ## Returns
        list(`sktmls.apis.Edge`)

        ## Example

        ```python
        # 모든 Edge 가져오기 (최대 100개로 제한)
        edges = graph_api_client.list_edges()

        # `hello` property가 `world`값을 가지며 `weight` property가 3보다 큰 Edge를 가져오기
        edges = graph_api_client.list_edges(query_params={
            "hello": "world",
            "weight__gte": 33,
        })
        ```
        """
        params = query_params
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        response = MLSResponse(
            requests.get(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges", params=params)
        ).results

        return [Edge(**e) for e in response["edges"]]

    def add_edge(self, frm: str, to: str, label: str, properties: Dict[str, Any] = {}) -> Edge:
        """
        Edge를 추가합니다.

        ## Args

        - frm: (str) Source Vertex의 고유 ID
        - to: (str) Target Vertex의 고유 ID
        - label: (str) Edge의 라벨
        - properties: (dict) Edge의 property 키와 값

        ## Returns
        `sktmls.apis.Edge`

        ## Example

        ```python
        edge = graph_api_client.add_edge(
            frm="USER001",
            to="USER002",
            label="follows",
            properties={
                "weight": 3,
                "hello": "world",
            }
        )
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.post(
                f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges",
                params=params,
                json={"from": frm, "to": to, "label": label, "properties": properties},
            )
        )

        return self.get_edge(f"{frm}_{label}_{to}")

    def drop_edges(self, query_params: Dict[str, Union[str, List[str]]] = {}) -> None:
        """
        조건에 해당하는 모든 Edge를 삭제합니다.

        ## Args

        - query_params: (optional) (dict) 쿼리 파라미터. 아래 예시 참조 (기본값: {})
            - {property_name}={value}: Vertex.Properties[property_name] == str(value)
            - {property_name}__{operator}
                - eq, gt, gte, lt, lte: Vertex.Properties[property_name] {operator} float(value)
                - bw: {property_name}__bw={value1},{value2}: float(value1) < Vertex.Properties[property_name] < float(value2)

        ## Example

        ```python
        # `hello` property가 `world`값을 가지며 `weight` property가 3보다 큰 Edge를 삭제하기
        edges = graph_api_client.delete_edges(query_params={
            "hello": "world",
            "weight__gte": 3,
        })
        ```
        """
        params = query_params
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(requests.delete(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges", params=params))

    def get_edge(self, edge_id: str) -> Edge:
        """
        단일 Edge를 가져옵니다.

        ## Args

        - edge_id: (str) Edge의 고유 ID. 보통은 `{source_vertex_id}_{label}_{target_vertex_id}` 형식을 따릅니다.

        ## Returns
        `sktmls.apis.Edge`

        ## Example

        ```python
        edge = graph_api_client.get_edge("USER001_follows_USER002")
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        response = MLSResponse(
            requests.get(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges/{edge_id}", params=params)
        ).results

        return Edge(**response["edges"][0])

    def update_edge(self, edge_id: str, properties: Dict[str, Any] = {}) -> Edge:
        """
        단일 Edge의 property를 업데이트합니다.

        ## Args

        - edge_id: (str) Edge의 고유 ID. 보통은 `{source_vertex_id}_{label}_{target_vertex_id}` 형식을 따릅니다.
        - properties: (dict) Edge의 property 키와 값

        ## Returns
        `sktmls.apis.Edge`

        ## Example

        ```python
        edge = graph_api_client.update_edge(
            edge_id="USER001_follows_USER002",
            properties={
                "weight": 5,
            }
        )
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.patch(
                f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges/{edge_id}",
                params=params,
                json={"properties": properties},
            )
        )

        return self.get_edge(edge_id)

    def drop_edge(self, edge_id: str) -> None:
        """
        단일 Edge를 삭제합니다.

        ## Args

        - edge_id: (str) Edge의 고유 ID. 보통은 `{source_vertex_id}_{label}_{target_vertex_id}` 형식을 따릅니다.

        ## Example

        ```python
        edge = graph_api_client.drop_edge("USER001_follows_USER002")
        ```
        """
        params = {}
        if self.__runtime_env != MLSRuntimeENV.MMS:
            params["mode"] = "test"

        MLSResponse(
            requests.delete(f"{self.config.MLS_GRAPH_API_URL[self.__env.value]}/v1/edges/{edge_id}", params=params)
        )
