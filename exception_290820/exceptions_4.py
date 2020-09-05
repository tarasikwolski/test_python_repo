def exception_ex4(my_dict: dict):
    key = "items"
    try:
        items = my_dict[key]
        for item in items:
            print(item)
    except KeyError as e:
        print(f'Key Error cached, more info: {e.args}')


def exception_ex4_v2(my_dict: dict):
    key = "items"
    items = my_dict.get(key, [])
    for item in items:
        print(item)


def main():
    exception_ex4_v2({"items": ["camera", "radio"]})
    exception_ex4_v2({"devices": ["camera", "radio"]})


if __name__ == "__main__":
    main()
