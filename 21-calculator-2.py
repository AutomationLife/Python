while True:
    print("""Calculator:
    +---------+
    0
    +---------+
    | [+] [-] |
    | [*] [/] |
    +---------+
    """)

    number1=float(input("First Number: "))
    operator=input("operator: ")
    number2=float(input("Second Number: "))
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

    again = input("Calculate again?: ")
    valid_answers = ("Yes", "yes", "Y", "y")
    if again not in valid_answers:
        break