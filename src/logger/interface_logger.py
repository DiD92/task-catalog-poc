import logging
import sys

if_logger = logging.getLogger(__name__)
if_logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

if_logger.addHandler(handler)
