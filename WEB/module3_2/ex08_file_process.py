from multiprocessing import Process
from multiprocessing.dummy import Pool
from threading import Thread
from time import time


def worker(values, filename):
    with open(filename, 'a') as f:
        for num in values:
            f.write(f'{num ** 2}\n')


if __name__ == '__main__':
    values = list(range(1800000))
    
    pl_filename = 'pl_squares.txt'
    timer = time()
    with Pool(3) as pool:
        result = pool.starmap(worker, [(values[:600000], pl_filename),
                                       (values[600000:1200000], pl_filename),
                                       (values[1200000:], pl_filename)])
    print(f'Done by 3 pool processes dummy: {round(time() - timer, 4)}')

    th_filename = 'th_squares.txt'
    threads = []
    step = 600000
    for i in range(1, 4):
        threads.append(Thread(target=worker, args=(values[(i - 1) * step: i * step], th_filename)))
    # threads = [
    #     ,
    #     Thread(target=worker, args=(values[600000:1200000], th_filename)),
    #     Thread(target=worker, args=(values[1200000:], th_filename)),
    # ])
    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f'Done by 3 threads: {round(time() - timer, 4)}')

    pr_filename = 'pr_squares.txt'
    processes  = []
    for i in range(1, 4):
        processes.append(
            Process(
                target=worker,
                args=(
                    values[(i - 1) * step : i * step],
                    pr_filename
                    )
                )
            )
    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    [process.close() for process in processes]
    print(f'Done by 3 processes: {round(time() - timer, 4)}')

    timer = time()
    worker(values, 'squares.txt')
    print(f'Done by 1 process: {round(time() - timer, 4)}')