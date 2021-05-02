import iamzero
from wrapt import wrap_function_wrapper


def wrapped_api_call(wrapped, instance, args, kwargs):
    try:
        result = wrapped(*args, **kwargs)
        return result
    except Exception as e:
        # add error to queue to be dispatched
        data = {
            "Service": instance._service_model.service_name,
            "Region": instance.meta.region_name,
            "Operation": args[0],
            "Parameters": args[1],
            "ExceptionMessage": e.response.get("Error", {}).get("Message"),
            "ExceptionCode": e.repsonse.get("Error", {}).get("Code"),
        }
        iamzero.send_event(data=data)
        raise


wrap_function_wrapper("botocore.client", "BaseClient._make_api_call", wrapped_api_call)
