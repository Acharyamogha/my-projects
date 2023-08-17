import re
def isphonenumber(num):
    if len(num) != 12:
        return False
    for i in range(len(num)):
        if i == 3 or i == 7:
            if num[i] != '-':
                return False
        else:
            if not num[i].isdigit():
                return False
    return True


def checkph(num):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pattern.match(num):
        return True
    else:
        return False


ph = input("Enter a phone number ")
if isphonenumber(ph):
    print("Valid phone number without using regular expresson")
else:
    print("Invalid phone number without using regular expresson")
print(" ")
if checkph(ph):
    print("Valid phone number using regular expresson")
else:
    print("Invalid phone number using regular expresson")
