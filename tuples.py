print("tuples () - cannot modify")

tup = (1,2,3)
print(tup)

tup = 1,2
print(tup)

tup = 1,
print(tup)

tup = (1,2,(3,4))
print("\n",tup)
print(tup[2][1])
print(tup[:1])

x,y,z = 1,2,3
print(x,y,z)

x,y,z = [1,2,3]
print(x)

tup1 = 1,2,3
tup2 = 4,5,6

print(tup1+tup2)
print(tup1*2)

print("\nmethods")
tup=(1,2,2,3,4)
print("no of times 2 occurred is ", tup.count(2))
print("index of 3 is", tup.index(3))
print("Length of tuple", len(tup))

print("\n Changing values in tuple")
tup=(1,2,2,3,4)
x = list(tup)
print("List of x", x)
x[2] = 5
print("New list", x)
tup = tuple(x)
print("new tuple", tup)