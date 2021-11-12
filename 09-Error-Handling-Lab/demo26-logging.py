# docs.python.org/3/howto/logging/html
import logging


def baba():
    logging.warning('function baba was called')
    return 'dqdo'

#debug
#info
#warning
#eror
#critical - tuk carshva sistemata


# tova sa nivata na debugvane, kolkoto po nadolu vurvim stava po seriozno

logging.basicConfig(filename='demo-logs.log', encoding='utf-8', level=logging.DEBUG)


# from functions import lru_cache
# da vidq za lru_cache