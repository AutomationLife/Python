print("Functions")
#Definig Function
def msg_input():
    print("EnterAnswer:")
#Calling Function
msg_input()
a = input()
print(a)

def hello(name):
    print("Hello", name)
hello("Abhi")

#Positional Arguments
def hello1(name, last):
    print("Hello", name, last)
hello1("Abhi", "happy")

#Keyword arguments
hello1(last="happy", name="Abhi")

#Arbitary arguments (*args)
def hello2(*name):
    print("Hi", name[1]) #can receive tuple of Arguments
hello2("Abhi", "happy")

#Arbitary arguments (**kwargs)
def hello3(**name):
    print("Hi", name["last"]) #can receive Dictionary of Arguments
hello3(first="Hello", last="Abhi")

#default parameter
def hello4(name, last="Mir"):
    print("Hi", name, last)

hello4("Adam")
hello4("Adam", "Smith")

def f(x):
    return 3*x

num = f(10)
print(num)

def f1(x):
    answer = 10*x
    return answer

print(f1(10))

def num_check(x):
    if x > 10:
        return True

print(num_check(20))