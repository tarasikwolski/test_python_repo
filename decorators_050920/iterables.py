from decorators_050920.my_iterables import MyIterable
from time import time, sleep


def iterable_ex1():
    dictionary = {1: "a",
                  2: "b",
                  3: "c"}
    for element in dictionary:
        print(f"element = {element}")

    for element in dictionary.keys():
        print(f"element = {element}")

    for element in dictionary.values():
        print(f"element = {element}")


def number_creator(n: int) -> list:
    numbers = []
    for number in range(n):
        numbers.append(number)
    return numbers


def iterable_ex2():
    print("Exercise 2")
    import sys
    numbers = number_creator(1000)
    print(f"size in list in bytes: {sys.getsizeof(numbers)}")
    print(f"size one number in bytes: {sys.getsizeof(1000)}")
    result = sum(numbers)
    print(f"result = {result}")


def iterable_ex3():
    print("Exercise 3")
    import sys
    my_iterator = MyIterable(1000)
    print(f"size in list in bytes: {sys.getsizeof(my_iterator)}")
    print(f"size one number in bytes: {sys.getsizeof(1000)}")
    result = sum(my_iterator)
    print(f"result = {result}")


def lazy_read_in_chuncks(fd, chuncks_size=1024):
    while True:
        data = fd.read(chuncks_size)
        if not data:
            break
        yield data


def generator_ex4():
    print("Exercise 4")
    with open("lorem") as fd:
        for piece in lazy_read_in_chuncks(fd):
            print(piece)
            sleep(1)


def generator_ex5():
    print("exercise 5")
    for line in open("lorem"):
        print(line, end="")
        sleep(1)


def main():
    # iterable_ex1()
    # iterable_ex2()
    # iterable_ex3()
    generator_ex4()
    generator_ex5()

if __name__ == "__main__":
    main()
