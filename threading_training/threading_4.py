from threading import Thread, Lock, Event
from time import sleep

name = ""
locker = Lock()
finish_event = Event()


def write_name():
    global name
    global locker
    global finish_event
    while True:
        try:
            in_name = input("write you name:\n ")
            if in_name == "exit":
                finish_event.set()
                break
            with locker:
                name = in_name
                print(f"Thread [write_name_loop] => Write new name is: {name}")
        except KeyboardInterrupt:
            finish_event.set()
            break


def read_name():
    global name
    global locker
    global finish_event
    old_name = ""
    while True:
        if finish_event.is_set():
            break
        locker.acquire()
        try:
            if old_name != name:
                print(f"Thread [check_name_loop] => old name {old_name}, new name: {name}")
                old_name = name
        finally:
            locker.release()
        sleep(1)


def thread_4():
    write_thread = Thread(target=write_name)
    read_thread = Thread(target=read_name)
    write_thread.start()
    read_thread.start()
    write_thread.join()
    write_thread.join()


def main():
    thread_4()


if __name__ == "__main__":
    main()
