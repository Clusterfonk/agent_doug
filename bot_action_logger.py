from logging.handlers import RotatingFileHandler
import logging
import os


def set_up_logger():
    logging.getLogger(__name__)
    logging.basicConfig(
        handlers=[RotatingFileHandler(filename=os.path.expanduser('~/.logs/agent_doug.log'),
                                      maxBytes=2000,
                                      backupCount=10)
                  ],
        format="[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )
