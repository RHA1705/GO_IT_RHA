from threading import Event, Thread
from time import sleep
from logger import logger


def worker_timeout(event: Event, time: float):
    while not event.is_set():
        logger.debug('Чекаємо поки прапорець event не буде встановлений')
        e_wait = event.wait(time)
        if e_wait:
            logger.debug('Починаємо виконувати якусь роботу')
        else:
            logger.debug('Прапорець ще не встановили чекаємо')


def worker(event: Event):
    logger.debug('waiting...')
    event.wait()
    # some work
    logger.debug('finished')


if __name__ == '__main__':
    e = Event()

    th = Thread(target=worker, args=(e, ))
    th.start()
    th_timeout = Thread(target=worker_timeout, args=(e, 1))
    th_timeout.start()

    sleep(3)
    e.set()

    logger.debug('End program')