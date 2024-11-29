import logging
import sys

import loguru


class InterceptHandler(logging.Handler):
    """Решение из официальной документации https://readthedocs.org/projects/loguru/downloads/pdf/stable/"""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = loguru.logger.level(record.levelname).name
        except ValueError:
            level = record.levelno  # type: ignore[assignment]
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore[assignment]
            depth += 1
        loguru.logger.opt(
            depth=depth,
            exception=record.exc_info,
        ).log(level, record.getMessage())


def setup_logging(config: dict) -> None:
    """Очистка логгера и обнуление корневого хендлера для stdout и stderr"""
    loguru.logger.remove()
    logging.root.handlers = []
    logging.root.setLevel(config["level"])
    for name in logging.root.manager.loggerDict:
        if logging.getLogger(name).hasHandlers():
            logging.getLogger(name).handlers.clear()
        logging.getLogger(name).handlers = [InterceptHandler()]
        logging.getLogger(name).propagate = False
    loguru.logger.configure(
        handlers=[{"sink": sys.stdout, "serialize": config["serializer"]}],
    )
