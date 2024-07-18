from threading import Semaphore, Thread
from time import sleep
from logger import logger


def worker(semaphore: Semaphore):
    logger.debug('Wait...')
    with semaphore:
        logger.debug('Got semaphore')
        sleep(1)
    logger.debug('finished')


if __name__ == '__main__':
    pool = Semaphore(2)

    threds = []
    for i in range(10):
        threds.append(Thread(target=worker, args=(pool, )))


    for w in threds:
        w.start()

    # w1.start()
    # w2.start()
    # w3.start()
    