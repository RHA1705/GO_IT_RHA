from random import randint
from threading import Thread
from logger import logger
from time import sleep


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None: #Metoda run konieczna do realizacji
        sleep(randint(1, 3))
        # logging.debug('Wake up!')
        logger.debug(f"In my thread: {self.args}")


if __name__ == '__main__':
    threads = []
    for i in range(5):
        th = MyThread(name=f"Th#{i}", args=f"Count thread - {i}") #daemon=True
        th.start()
        threads.append(th)

    # [th.join() for th in threads]
    sleep(2)
    logger.debug('End program')
