#Strings
print("string or string")

#Integers - whole number
print("\ninteger")
print(42000)
print(42_000)
print(+42000)
print(+42_000)
print(-42000)
print(-42_000)

#float - decimal numbers
print("\nfloat")
print(4.2)
print(-4.2)
print(1.0)
print(1.)

#Exponential
print("\nExponential") # Outpus float
print(4E2)
print(4e2) #value after E/e should be integer
print(4.2E2) #base can be int or float

#Type Casting
print("\nimplicti/automatic")
print(4+4.2)

print("\nExplicit/Casting")
print("\nint()")
print(int("4"))
print(int(4.9))

print("\nfloat()")
print(float("4"))
print(float("4.9"))

print("\nstr()")
print(str(4))
print(str(4.9))

print("\ntype()") #to check data type
print(type(4))
print(type(4.9))
print(type("hi"))

#We use bool() method.
print("\b bool()")
print("True conditions")
print(bool(1))

print("\nFalse Conditions")
print(bool(False))
print(bool(0))
print(bool())
print(bool(None))

x = None
print("Type of None type", type(x))