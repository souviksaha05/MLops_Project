from us_visa.logger import logging

#logging.info("welcome to our custom log")

from us_visa.exception import USvisaException
import sys

try: 
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)