import logging
from pathlib import Path


def get_logger(name:str)->logging.Logger:
    logger=logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger
    project_root=Path(__file__).resolve().parents[2]
    log_directory=project_root/"logs"
    log_directory.mkdir(exist_ok=True)
    log_file=log_directory/"framework.log"
    formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(funcName)s | %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

       # Attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
