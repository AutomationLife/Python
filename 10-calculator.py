print("""Calculator:
+---------+
0
+---------+
| [+] [-] |
| [*] [/] |
+---------+
""")

print("First nummber: 558.28")
print("Operator: +")
print("Second number: 452.64")
print("\nAnswer:")
print("+---------+")
print(558.28+452.64)
print("+---------+")

print("\n")
number1=float(input("First Number: "))
print("Operator: +")
number2=float(input("Second Number: "))
total=number1+number2
print("\nAnswer:")
print("+---------+")
print(total)
print("+---------+")

print("\n")
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