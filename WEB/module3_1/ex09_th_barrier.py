from random import randint
from threading import Barrier, Thread, current_thread
from time import sleep, ctime

from logger import logger


def worker(barrier: Barrier):
    name = current_thread().name
    logger.debug(f"Start thread {name}: {ctime()}")
    sleep(randint(1, 3))
    num = barrier.wait()
    logger.debug(f"{num}")
    logger.debug(f'Бар\'єр подоланий {name}: {ctime()}')


if __name__ == '__main__':
    br = Barrier(2)

    for i in range(9):
        th = Thread(target=worker, args=(br, ))
        th.start()
