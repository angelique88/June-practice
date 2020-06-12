# Create a function that takes two parameters and, if both parameters are strings,
# add them as if they were integers or if the two parameters are integers, concatenate them.


def add(a, b):
    if (type(a) == str) and (type(b) ==str):
        return int(a) + int(b)
    elif (type(a) == int) and (type(b) ==int):
        return str(a) + str(b)
    else:
        return None


print(add(3, "4"))

print(add("3", "4"))

print(add(3, 4))