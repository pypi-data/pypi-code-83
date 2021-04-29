import os
import signal
import threading
import json

from routes_common import *

import azureml.contrib.services.aml_request as aml_request
from azureml.contrib.services.aml_request  import AMLRequest
from azureml.contrib.services.aml_response import AMLResponse
from werkzeug.http import parse_options_header
from .framework import request, g, Response


@main.route('/score', methods=['GET'])
def get_prediction_realtime():
    service_input = get_service_input_from_url(g, request, aml_request._rawHttpRequested)

    # run the user-provided run function
    return run_scoring(service_input, request.headers, request.environ.get('REQUEST_ID', '00000000-0000-0000-0000-000000000000'))


@main.route('/score', methods=['POST'])
def score_realtime():
    g.apiName = "/score"

    if aml_request._rawHttpRequested:
        service_input = request
        service_input.__class__ = AMLRequest # upcast
    else:
        # enforce content-type json as either the sdk or the user code is expected to json deserialize this
        main.logger.info("Validation Request Content-Type")
        if 'Content-Type' not in request.headers or parse_options_header(request.headers['Content-Type'])[0] != 'application/json':
            return AMLResponse({"message": "Expects Content-Type to be application/json"}, 415, json_str=True)

        if main.request_is_parsed_json:
            service_input = request.get_json()
        else:
            # expect the response to be utf-8 encodeable
            service_input = request.data.decode("utf-8")

    # run the user-provided run function
    return run_scoring(service_input, request.headers, request.environ.get('REQUEST_ID', '00000000-0000-0000-0000-000000000000'))


@main.route('/score', methods=['OPTIONS'])
def score_options_realtime():
    g.apiName = "/score"

    if aml_request._rawHttpRequested:
        service_input = request
        service_input.__class__ = AMLRequest # upcast
    else:
        return AMLResponse("Method not allowed", 405, json_str=True)

    # run the user-provided run function
    return run_scoring(service_input, request.headers, request.environ.get('REQUEST_ID', '00000000-0000-0000-0000-000000000000'))


def run_scoring(service_input, request_headers, request_id=None):
    main.start_hooks(request_id)

    try:
        response = invoke_user_with_timer(service_input, request_headers)
        main.appinsights_client.send_model_data_log(request_id, service_input, response)
    except ClientSideException:
        raise
    except ServerSideException:
        raise
    except TimeoutException:
        main.stop_hooks()
        main.send_exception_to_app_insights(request_id)
        raise
    except Exception as exc:
        main.stop_hooks()
        main.send_exception_to_app_insights(request_id)
        raise RunFunctionException(str(exc))
    finally:
        main.stop_hooks()

    if isinstance(response, Response): # this covers both AMLResponse and flask.Response
        main.logger.info("run() output is HTTP Response")
        return response

    return wrap_response(response)


def invoke_user_with_timer(input, headers):
    params = prepare_user_params(input, headers, aml_request._rawHttpRequested)

    # Signals can only be used in the main thread.
    if os.name != 'nt' and threading.current_thread() is threading.main_thread():
        old_handler = signal.signal(signal.SIGALRM, alarm_handler)
        signal.setitimer(signal.ITIMER_REAL, main.scoring_timeout_in_ms / 1000)
        main.logger.info("Scoring Timer is set to {} seconds".format(main.scoring_timeout_in_ms / 1000))

        result = user_main.run(**params)

        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old_handler)

    else:
        watchdog = Watchdog(main.scoring_timeout_in_ms / 1000)

        try:
            result = user_main.run(**params)
        except Watchdog:
            error_message = "Scoring timeout after {} ms".format(main.scoring_timeout_in_ms)
            raise TimeoutException(error_message)
        finally:
            watchdog.stop()

    return result


# Errors from Server Side
@main.errorhandler(ServerSideException)
def handle_exception(error):
    return handle_server_exception(error)

# Errors from Client Request
@main.errorhandler(ClientSideException)
def handle_exception(error):
    return handle_client_exception(error)


# Errors from User Run Function
@main.errorhandler(RunFunctionException)
def handle_exception(error):
    return handle_run_exception(error)


# Errors of Scoring Timeout
@main.errorhandler(TimeoutException)
def handle_exception(error):
    return handle_timeout_exception(error)


# Unhandled Error
# catch all unhandled exceptions here and return the stack encountered in the response body
@main.errorhandler(Exception)
def unhandled_exception(error):
    return all_unhandled_exception(error)
