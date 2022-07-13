print("Loops")
print("while loop")
temp = 50
while temp > 25:
    print("Current temperature: ", temp)
    print("Ice cube added.")
    temp -= 5

print("Temperature reached 25C")

print("\nwhile else loop")
x = 0
while x != 5:
    x+=1
    print(x, " loop ran")
else:
    print("else ran")

print("\n break statement")
x = 0
while x != 5:
    x+=1
    if x == 3:
        break
    print(x, " loop ran")
else:
    print("else ran")

print("\n continue statement")
x = 0
while x != 5:
    x+=1
    if x == 3:
        continue
    print(x, " loop ran")
else:
    print("else ran")