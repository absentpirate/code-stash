def main():
    user_input1 = int(input("num1: "))
    user_input2 = int(input("num2: "))

    user_option = chr(input("symbol(+/-/*): "))

    print("answer: ", end="")

    if user_option == '+':
        print(addition(num1, num2))
    elif user_option == '-':
        ...
    elif user_option == "*":
        print(multipication(num1, num2))
    else:
        print("Invalid option")

    
def addition(num1, num2):
    return num1+num2

def multipication(num1, num2):
    return num1*num2

main()