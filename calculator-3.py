def display_calc():
    print("""Calculator:
    +---------+
    0
    +---------+
    | [+] [-] |
    | [*] [/] |
    +---------+
    """)

def user_input():
    number1=float(input("First Number: "))
    operator=input("operator: ")
    number2=float(input("Second Number: "))
    calculate(number1, operator, number2)
    
def calculate(number1, operator, number2):   
    if operator == "+":
        total=number1+number2
    elif operator == "-":
        total=number1-number2
    elif operator == "*":
        total=number1*number2
    elif operator == "/":
        total=number1/number2
    else:
        total="Invalid Operator"
    print("\nAnswer:")
    print("+---------+")
    print(total)
    print("+---------+")

def calculate_again():
    again = input("Calculate again?: ")
    valid_answers = ("Yes", "yes", "Y", "y")
    if again not in valid_answers:
        return False

while True:
    display_calc()
    user_input()
    again = calculate_again()
    if again == False:
        break
