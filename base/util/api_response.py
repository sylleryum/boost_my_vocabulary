def error_response(trace_id, error_message, details=''):
    return {"trace_id": trace_id,
            "error": error_message,
            "additional_details": details}


def results_response(data):
    return {"results": data}
