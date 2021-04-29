# src/api/routes/authors.py
from flask import Blueprint
from flask import request
import sys

sys.path.append('..')
from src.pylong.api import response_with
from src.pylong.api.utils import responses as resp
from src.pylong.api import list_case, update_case

case_routes = Blueprint("case_routes", __name__)


@case_routes.route('/update', methods=['POST'])
def update_cases():
    try:
        data = request.get_json()
        result = update_case(data)
        return response_with(resp.SUCCESS_201, value={"result":
                                                          result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@case_routes.route('/list', methods=['GET'])
def list_cases():
    try:
        data = request.get_json()
        result = list_case(data)
        return response_with(resp.SUCCESS_201, value={"result":
                                                          result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
