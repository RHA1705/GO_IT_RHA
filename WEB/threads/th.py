from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Обробляємо файл {filename}')
    # отримуємо вміст файлу
    with open(filename, 'r') as f:
        content = f.read()

    # заміняємо substr на new_substr
    content = content.replace(substr, new_substr)

    # записуємо дані в файл
    with open(filename, 'w') as f:
        f.write(content)


def main():
    filenames = [
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test1.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test2.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test3.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test4.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test5.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test6.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test7.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test8.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test9.txt',
        'C:/Users/ROMAN/Repositories/GO_IT_RHA/WEB/threads/test10.txt',
    ]

    threads = [Thread(target=replace, args=(filename, 'id', 'ids'))
                for filename in filenames]

        # запускаємо потоки
    for thread in threads:
            thread.start()

        # чекаємо завершення потоків
    for thread in threads:
            thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'Выполнение заняло {end_time- start_time :0.2f} секунд.')