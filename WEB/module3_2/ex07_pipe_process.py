from multiprocessing import Process, Pipe
from time import sleep
import sys


def worker(conn1: Pipe, conn2: Pipe, name):
    print(f'{name} started!')
    if name == 'first':
        conn2.send(10)
    val = conn1.recv()
    print(f'{name} {val ** 2}')
    conn2.send(30)
    sys.exit(0)


if __name__ == '__main__':
    rcv1, snd1 = Pipe()
    rcv2, snd2 = Pipe()

    pr1 = Process(target=worker, args=(rcv1, snd2, 'first'))
    pr2 = Process(target=worker, args=(rcv2, snd1,  'second'))

    pr1.start()
    pr2.start()

    # snd1.send(10)
    sleep(2)
    # snd2.send(5)
