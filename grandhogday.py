import time

perfect_number = 12_395

clock1 = """
+---+---+---+
| 5 | 5 | 9 |
+---+---+---+
"""

clock2 = """
+---+---+---+
| 6 | 0 | 0 |
+---+---+---+
"""

print("""
+---------------------------------+
|Welcome to Groundhog Day - 2 Feb.|
|You're struck in 2 February 2020.|
|Enter the perfect number to end  |
|the loop or be struck forever... |
+---------------------------------+
""")

number = int(input("Enter Number: "))

while number != perfect_number:
    if number < perfect_number:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print("February 2\nNumber too low.\n")
    else:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print("February 2\nNumber too high.\n")
    
    number = int(input("Enter Number: "))

print(clock1)
time.sleep(1)
print(clock2)
time.sleep(1)
print("February 3\nToday is tomorrow.\n")
