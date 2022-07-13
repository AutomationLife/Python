print("dictionary {key:value}")
print('{"hello":"hola", "page":112}')
#Key should be unique
#can be any data-type except list
#Its one way, meant can search only using key but not by values
#They are ordered, print in the order they are given
#Can be written in multi-line

data = {
    "key":{"nested":"key1"}
}
print(data["key"])

data["key"] = "new value"
print(data)

data["new"] = "val"
print(data)

del data["key"]
print(data)

for i in data:
    print(i)

print("\nmethods")

data = {
    "one": 1,
    "two": 2,
    "three": 3
}
print(data.keys())
print(data.values())
print(data.get("two"))

data.pop("three")
print(data)

data.popitem() # remove last item
print(data)