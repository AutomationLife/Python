print("Lists [] - any data type can be added")

data = [1, 1.0,"one",[1]]
print('\nlist : ', data)
print("position 1", data[0])
print("Nested list", data[3][0])

data[2] = "two"
print('new list : ', data)

print("\ndelete a value from list")
del data[2]
print('new list : ', data)

print("\nlist indexing")

data1 = list(range(1,11))
print("list : ", data1)
print("length of list", len(data1))

print("Last value", data1[-1])

print("Range of list:", data1[1:3]) #returns a new list from start index to end index-1 value

print("\nList Methods")
print("append() - adds end of list")
x = []
x.append(1)
x.append(1.0)
x.append(3)
print(x)

print("\ninsert(location, value)")
x.insert(1, 33)
print(x)

print("\nsort() - ascending")
x.sort()
print(x)

print("\nremove() - searches by value, first occurance")
x.remove(3)
print(x)

print("\npop() - serches by index, returns value and deletes")
x.pop(1)
print(x)

print("\ndel method")
del x[1]
print(x)

print("\ncopy() - copies existing list")
x=[1,2,3,4,5]
y=x.copy()
print(y)

print("\nlist() - function that copies existing list")
x=[1,2,3,4,5]
y=list(x)
print(y)


print("\nSlice[:]")
print("copy - [:]")
y = x[:]
print(y)

print("\nmore usages")
y = x[:3]
print(y)

y = x[3:]
print(y)

y = x[:-1]
print(y)

del y[:]
print(y)

print("\nJoin and Multiply list")
x = [1,2,3]
y = [4,5,6]

print("join", x+y)
x.extend(y)
print("Extend method", x)

print("\nmultiply", y * 2)


print("\nMembership Operators")
print("in , not in")
num_list = [1,2,3,4,5]
print(3 in num_list)
print(3 not in num_list)

print("he" in "hello")


print("\n for loop with list")
num_list = []
for num in range(1,6):
    num_list.append(num)
print(num_list)

num_list = []
for num in range(1,6):
    num_list.insert(0,num)
print(num_list)

num_list = []
for num in range(1,6):
    num_list.insert(5,num)
print(num_list)

list_val = ["hi","hello","bye"]
for x in list_val:
    print(x)

print("\n Smallest in list")
num_list = [187,0,8,1,9,9,9,1]
smallest = num_list[0]
for num in num_list:
    if num < smallest:
        smallest = num
print(smallest)

print("\n prinnt new list from old list with no repetation")
num_list=[1,8,1,8,7,7]
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)

print(new_list)


print("\n List comprehension")
print("for loop")
num_list = [num * 2 for num in range(1,6)]
print(num_list)

print("\nConditionals")
num_list = [num for num in range(10) if num % 2 == 1]
print(num_list)

print("\ncomparing lists")
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8,10]

print("\nall()")
print(all(num in list2 for num in list1)) # all num in list1 are not in list 2
print(all(num in list1 for num in list2))

print("\nany()")
print(any(num in list2 for num in list1))
print(any(num in list1 for num in list2))