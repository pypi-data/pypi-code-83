import inspect
from typing import Callable, Optional, Tuple, Type

from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from tortoise import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.query_utils import Q

from fast_tmp.depends.auth import get_user_has_perms
from fast_tmp.utils.pydantic_creator import pydantic_offsetlimit_creator


def add_filter(func: Callable, filters: Optional[Tuple[str, ...]] = None):
    signature = inspect.signature(func)
    res = []
    for k, v in signature.parameters.items():
        if k == "kwargs":
            continue
        res.append(v)
    if filters:
        for filter_ in filters:
            res.append(
                inspect.Parameter(
                    filter_, kind=inspect.Parameter.KEYWORD_ONLY, annotation=str, default="__null__"
                )
            )
    # noinspection Mypy,PyArgumentList
    func.__signature__ = inspect.Signature(parameters=res, __validate_parameters__=False)


def create_pydantic_schema(
    model: Type[Model],
    name: str,
    fields: Optional[Tuple[str, ...]] = None,
    exclude_readonly: bool = False,
) -> Type[BaseModel]:
    if fields:
        return pydantic_model_creator(
            model, name=name, include=fields, exclude_readonly=exclude_readonly
        )
    else:
        return pydantic_model_creator(model, name=name, exclude_readonly=exclude_readonly)


def create_list_route_with_page(
    route: APIRouter,
    path: str,
    model: Type[Model],
    fields: Optional[Tuple[str, ...]] = None,
    codenames: Optional[Tuple[str, ...]] = None,
    searchs: Optional[Tuple[str, ...]] = None,
    filters: Optional[Tuple[str, ...]] = None,
    res_pydantic_model: Optional[Type[BaseModel]] = None,
    random_str: str = "",
):
    """
    创建list的路由
    """
    if res_pydantic_model:
        schema = res_pydantic_model
    else:
        schema = create_pydantic_schema(
            model,
            f"CREATORList{model.__name__}{path.replace('/', '_')}Page{random_str}",
            fields=fields,
        )
    paging_schema = pydantic_offsetlimit_creator(schema)

    async def model_list(
        offset: int = 0,
        limit: int = 10,
        search: Optional[str] = None,
        **kwargs,
    ):
        count = model.all()
        query = model.all().limit(limit).offset(offset)
        if search and searchs:
            x = [Q(**{f"{i}__contains": search}) for i in searchs]
            if x:
                q = x[0]
                for i in x[1:]:
                    q = q | i
                query = query.filter(q)
                count = count.filter(q)
        if kwargs:
            s = {}
            for k, v in kwargs.items():
                if not v == "__null__":
                    s[k] = v
                else:
                    pass
            if s:
                query = query.filter(**s)
                count = count.filter(**s)

        data = await query
        return paging_schema(total=await count.count(), data=[schema.from_orm(i) for i in data])

    add_filter(model_list, filters)
    route.get(
        path, dependencies=[Depends(get_user_has_perms(codenames))], response_model=paging_schema
    )(model_list)
