from threading import Event, Thread
from time import sleep
from logger import logger


def master(event: Event):
    sleep(1)  # Some work
    logger.debug('Set event...')
    event.set()


def worker(event: Event):
    logger.debug('waiting...')
    event.wait()
    # some work
    logger.debug('finished')


if __name__ == '__main__':
    e = Event()

    m = Thread(target=master, args=(e, ))
    w2 = Thread(target=worker, args=(e, ))
    w1 = Thread(target=worker, args=(e, ))

    w1.start()
    w2.start()
    m.start()
