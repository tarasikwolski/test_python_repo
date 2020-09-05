def exceptions_f1():
    nums = [1, 2, 3, 4, 5]
    print(nums[5])


def exceptions_f2(name: str):
    if not name:
        raise ValueError("Empty name is invalid")


def exception_f3(value1: int, value2: int):
    return value1 / value2


def main():
    try:
        exceptions_f1()
    except (IndexError, Exception) as e:
        print(f"Mój błąd, więcej info: {e.args}")
    try:
        exceptions_f2("Zdzisława")
    except ValueError as e:
        print(f"Kolejny błąd")
    try:
        exception_f3(10, 1)
    except ZeroDivisionError as e:
        print(f"Błąd w dzieleniu, more info: {e.args}")


if __name__ == '__main__':
    main()
