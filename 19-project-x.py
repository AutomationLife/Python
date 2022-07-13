vip = ["Thomas", "Costa", "Jon"]
vip_total = len(vip)

guests_max = 5

guests = []
guests_total = len(guests)
vip_entered = 0

title = "-Security Check-"
print("-"*len(title))
print(title)
print("-"*len(title))


while guests_total < guests_max:
    name = input("Whats your name?\n")
    name = name.capitalize()

    if name == "" or name.isalpha() == False:
        print("I need a real name.")
    elif name in vip:
        guests.append(name)
        guests_total += 1
        vip_entered += 1
        print(f"Welcome to the party {name}! Go right in.")
    elif name not in vip:
        if guests_total + (vip_total - vip_entered) < guests_max:
            guests.append(name)
            guests_total += 1
            print(f"You're not in the list {name}! but go in.")
        else:
            print(f"Sorry {name}, spaces only for VIP guest.")

message = "No more guests allowed!"
print("-"*len(message))
print(message)
print("-"*len(message))

print("Party Guests:")
guests.sort()
for names in guests:
    print(names)
print("Total:", guests_total)