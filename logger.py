import logging
import os
from logging.handlers import RotatingFileHandler


def set_up_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        handlers=[RotatingFileHandler(filename=os.path.expanduser('~/.logs/agent_doug.log'),
                                      maxBytes=2000,
                                      backupCount=10)
                  ],
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )