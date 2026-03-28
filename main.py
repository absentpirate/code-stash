def main():
    user_input1 = int(input("num1: "))
    user_input2 = int(input("num2: "))

    user_option = input("symbol(+/-/*): ")

    print("answer: ", end="")

    if user_option == '+':
        print(addition(user_input1, user_input2))
    elif user_option == '-':
        print(subtract(user_input1, user_input2))
    elif user_option == "*":
        print(multipication(user_input1, user_input2))
    else:
        print("Invalid option")
        print("Valid options are: +, -, *")

    print("~~ Rerun the program to continue~~")

    


def multipication(num1, num2):
    return num1*num2
def subtract(num1, num2):
    return num1-num2

    
def addition(num1, num2):
    return num1+num2

main()