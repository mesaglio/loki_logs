from functools import wraps
from flask import request
from utils.logger import logger


def log_enpoint_information(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{request.remote_addr} - {request.path}")
        return func(*args, **kwargs)

    return wrapper
