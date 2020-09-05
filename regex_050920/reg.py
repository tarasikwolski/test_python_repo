import re
def re_ex1():
    print("write number")
    value = input("write number >>")
    expression = "[0-9]+"
    if re.match(expression, value):
        if int(value) %2 ==0:
            print("even number")
        else:
            print("odd")
    else:
        print("Incorrect")

def re_ex2():
    post_code = input("post code >>")
    expression = "[0-9]{2}\\-[0-9]{3}"
    if re.match(expression, post_code):
        print("Its fine")
    else:
        print("not fine")

def main():
    #re_ex1()
    re_ex2()

if __name__ == "__main__":
    main()
