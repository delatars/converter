import logging
import sys


def init_loggers(debug_mode=False):
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] [%(name)s] %(message)s"))
    logging.root.addHandler(stdout_handler)
    logging.root.setLevel(logging.DEBUG if debug_mode else logging.INFO)
