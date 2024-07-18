import sys
from multiprocessing import Process
import os
from time import sleep


def example_work(params):
    sleep(15)
    print(params)
    sys.exit(0)


if __name__ == '__main__':
    prs = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process - {i}",))  # daemon=True
        pr.start()
        prs.append(pr)

    sleep(5)
    process_pid = prs[2].pid
    os.kill(process_pid, 9) #poczytac wiecej na temat funkcji
    [pr.join() for pr in prs]

    print('End program')