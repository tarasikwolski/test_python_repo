import re


def re_ex1():
    print("write number")
    value = input("write number >>")
    expression = "[0-9]+"
    if re.match(expression, value):
        if int(value) % 2 == 0:
            print("even number")
        else:
            print("odd")
    else:
        print("Incorrect")


# def re_ex2():
#     post_code = input("post code >>")
#     expression = "[0-9]{2}\\-[0-9]{3}"
#     if re.match(expression, post_code):
#         print("Its fine")
#     else:
#         print("not fine")

def reg_ex3():
    login = input("Login: ")
    if re.match(r"[0-9a-zA-Z]{8-16}", login):
        print("correct")
        print(len(login))
    else:
        print("wrong")


def regex_ex4():
    print('Write something with ala')
    value = input()
    expression = '.*ala.*'
    if re.match(expression, value):
        print('ala found')
    else:
        print('ala not found')


def regex_ex5():
    print('Write date')
    value = input()
    expression = '([0-9]{2}\.){2}[0-9]{4}r\.'
    if re.match(expression, value):
        print('date found')
    else:
        print('date not found')


def regex_ex6():
    print('Write serial id')
    value = input()
    expression = '[A-Z]{3}[0-9]{5}[a-z]{1}[A-Z]{1}'
    if re.match(expression, value):
        print('correct serial id')
    else:
        print('incorrect serial id')


def regex_ex7():
    print('Write serial')
    value = input()
    expression = '([A-Z0-9!@#\\$%\\^&\\*]{5}\\-){4}[A-Z0-9!@#\\$%\\^&\\*]'
    if re.match(expression, value):
        print('correct serial')
    else:
        print('incorrect serial')


def regex_ex8():
    print('Write FV')
    value = input()
    expression = 'FV/[0-9]+/[0-9]{2}/[0-9]{4}'
    if re.match(expression, value):
        print('correct FV')
    else:
        print('incorrect FV')


# “Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś teorię, okazuje się jasne.”

def reg_ex9():
    text = input()
    regex = " "
    result = re.split(regex, text)
    print(result)
    print(f"Ilosc slow: {len(result)}")
    print(f"ilosc znakow: {len(text)}")
    longest_word = " "
    shortest_word = result[0]
    sum_of_charts = 0
    for word in result:
        if len(longest_word) < len(word):
            longest_word = word
        if len(shortest_word) > len(word):
            shortest_word = word
        sum_of_charts += len(word)
    print(f"najdluzsze slowo: {longest_word}")
    print(f"najkrotsze  slowo: {shortest_word}")
    average = sum_of_charts / len(result)
    print(f"srednia :{average}")


def main():
    # re_ex1()
    # re_ex2()
    # reg_ex3()
    # regex_ex4()
    # regex_ex5()
    # regex_ex6()
    # regex_ex7()
    # regex_ex8()
    reg_ex9()


if __name__ == "__main__":
    main()
