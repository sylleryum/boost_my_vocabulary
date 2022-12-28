import logging

from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response

from base import literals
from base.exceptions import InvalidKeyException, ResourceDuplicatedException
from base.util.api_response import error_response
from base.util.trace_id_generator import write_error


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if InvalidKeyException(exc):
        message = exc.args[0]

        trace_id = write_error(message)
        return Response(error_response(trace_id, message),
                        status=status.HTTP_400_BAD_REQUEST)

    if ResourceDuplicatedException(exc):
        message = exc.args[0]
        logging.error(f"{message} {exc}")
        return Response(error_response(message),
                        status=status.HTTP_400_BAD_REQUEST)

    # returns response as handled normally by the framework
    return response
