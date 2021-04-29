#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonpath_expression.jsonpath_expression import JsonpathExpression

if  __name__ == "__main__" :
    js = JsonpathExpression()
    str1='{}'
    dic = js.jsonpath_expression(str1,1)
    js.test_jsonpath_expression(str1,dic)
