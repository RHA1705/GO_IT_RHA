from threading import Timer
from time import sleep
from logger import logger



def worker(param):
    logger.debug(param)


if __name__ == '__main__':
    one = Timer(0.5, worker, args=('one param', ))
    one.name = 'First thread'
    one.start()

    two = Timer(1, worker, args=('two param', ))
    two.name = 'Second thread'
    two.start()
    sleep(1.5)
    two.cancel()
    logger.debug('End program')
