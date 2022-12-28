import logging
import uuid


def write_error(message):
    trace_id = uuid.uuid4()
    logging.debug(f"trace_id: {trace_id}, error: {message}", exc_info=True)
    return trace_id


def write_debug(message):
    trace_id = uuid.uuid4()
    logging.debug('--')
    logging.debug(f"trace_id: {trace_id}, debug: {message}", exc_info=True)
    logging.debug('--')
    return trace_id
