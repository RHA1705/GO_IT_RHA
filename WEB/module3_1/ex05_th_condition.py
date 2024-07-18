from threading import Condition, Thread
from time import sleep
from logger import logger


def master_th(con: Condition):
    logger.debug('Master work hard')
    sleep(1)
    with con:
        logger.debug('Ще працюйте!')
        # con.notify_all()
        con.notify()
        sleep(2)
        logger.debug('Ще працюйте!')
        con.notify()


def worker(con: Condition):
    logger.debug('waiting...')
    with con:
        con.wait()
        # some work
        logger.debug('finished')


if __name__ == '__main__':
    con = Condition()

    master = Thread(target=master_th, args=(con, ))

    w1 = Thread(target=worker, args=(con, ))
    w2 = Thread(target=worker, args=(con, ))

    w1.start()
    w2.start()
    master.start()
    