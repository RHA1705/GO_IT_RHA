from random import randint
from time import sleep
from threading import Thread



def th_function(param):
    sleep(randint(2, 5))
    print(param)


if __name__ == "__main__":
    for i in range(5):
        th = Thread(target=th_function, args=(i, ))
        th.start()
        print(th.ident)
