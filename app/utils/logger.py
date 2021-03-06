"""Module to handle logging functionality"""
import logging
import os


def get_logger():
    """Get object of logger"""
    logger_obj = logging.getLogger("Person Logger")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handle = logging.StreamHandler()
    console_handle.setFormatter(formatter)
    logger_obj.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
    logger_obj.addHandler(console_handle)
    return logger_obj

