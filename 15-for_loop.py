print("for loop")
for letters in "Abhijith":
    print(letters)

name = "Boss"
for letters in name:
    print(letters)

print("\nfor-else loop, break")
name = "BigBoss"
for letters in name:
    if letters == "g":
        break
    print(letters)
else:
    print("Else ran")

print("\nfor-else loop, continue")
name = "BigBoss"
for letters in name:
    if letters == "g":
        continue
    print(letters)
else:
    print("Else ran")

print("\nrange function")
for num in range(6):
    print("Loop", num)

print("\n")

for num in range(1,6): # (start, end) , start < end
    print("Loop", num)

print("\n")

for num in range(6,1,-2): # (start, end, step) 
    print("Loop", num)

print("\n")

x = 1
for num in range(x,6):
    print("Loop", num)