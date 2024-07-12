from threading import Thread
import logging
from time import sleep


'''Ecample 3'''
from threading import Thread
from time import sleep
import logging


class UsefulClass():
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        logging.debug('Wake up!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t2 = UsefulClass(2)
    thread = Thread(target=t2)
    thread.start()
    print('Some stuff')

'''Example 2. Thread like a class'''
# class MyThread(Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
#         super().__init__(group=group, target=target, name=name, daemon=daemon)
#         self.args = args
#         self.kwargs = kwargs

#     def run(self) -> None:
#         sleep(2)
#         logging.debug('Wake up!')
#         logging.debug(f"args: {self.args}")


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(5):
#         thread = MyThread(args=(f"Count thread - {i}",))
#         thread.start()
#     print('Usefull message')


'''Example 1. Thread like a function'''
# def worker(param):
#     print(param)


# if __name__ == '__main__':
#     for i in range(5):
#         th = Thread(target=worker, args=(f"Count thread - {i}", ))
#         th.start()        