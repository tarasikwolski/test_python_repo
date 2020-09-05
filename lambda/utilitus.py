def lambda_ex1():
    names = ["Jan", "Jacek", "Dorota", "Krystian", "Krzystof", "Grzegorz", ""]
    print("results a")
    result_a = sorted(names, key=lambda name: len(name))
    print(result_a)

    print("results b")
    result_b = sorted(names, key=lambda name: len(name), reverse=True)
    print(result_b)

    print("results c")
    result_c = sorted(names, key=lambda name: name[0] if len(name) >0 else "")
    print(result_c)

    print("results c*")
    result_c_ = sorted(names, key=lambda name: name)
    print(result_c_)


def main():
    lambda_ex1()


if __name__ == "__main__":
    main()
