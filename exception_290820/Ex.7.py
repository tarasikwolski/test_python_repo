def exceptions_f7():
    fd = None
    try:
        fd = open("test.txt")
    except IOError as e:
        print(f"Exception catcher {e.args}")
    finally:
        if fd is not None:
            fd.close()

def exceptions_f7_v2():
    try:

        with open("testy.txt") as fd:
            print("plik w tym miejscu juz jest otwarty")
    except IOError as e:
        print(f"Exception while reading file {e.args}")


if __name__ == "__main__":
    main()
