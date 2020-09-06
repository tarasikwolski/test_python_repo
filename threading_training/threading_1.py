from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from random import randint
from threading import Thread
from time import sleep


class MyThread(Thread):
    def run(self):
        for i in range(5):
            print(f'class thread - i number ={i},random number = {randint(10, 100)}\n')
            sleep(1)


def thread_1():
    my_thread = MyThread()
    my_thread.start()
    # my_thread.join()
    print('koniec metory urucamiającej thread')


def my_target_func(how_many=5):
    for i in range(how_many):
        print(f'thread from function - i number ={i},random number = {randint(10, 100)}\n')
        sleep(1)


def thread_2():
    origin_thread = Thread(target=my_target_func, args=(5,))
    origin_thread.start()


def my_sleeping_thread(thread_number: int):
    while True:
        sleep(randint(1, 10))
        print(f'[thread_number={thread_number}]: date_now="{datetime.now()}"\n')


def thread_3():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(5):
            executor.submit(my_sleeping_thread, index)


def main():
    thread_3()
    print('koniec main')

if __name__ == "__main__":
    main()
