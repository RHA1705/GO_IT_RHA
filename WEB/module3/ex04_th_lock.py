from random import randint
from threading import Thread, RLock
from logger import logger
from time import sleep

counter =  0
lock = RLock()


def worker():
    global counter
    while True:
        #lock.acquire()
        with lock:
            counter += 1
            sleep(randint(1, 3))
            with open('result.txt', 'a') as fd:
                fd.write(f'{counter}\n')
        #lock.relese()


if __name__ == '__main__':
    logger.debug('Start program')
    for i in range(5):
        th = Thread(name=f"Th#{i}", target=worker)
        th.start()
    
    logger.debug('End program')
