
text = input("Enter anything: ")
text = text.lower()

x = text.count('x')
o = text.count('o')

print("Number of X:", x)
print("Number of O:", o)

if x == o:
    print("Same number of X and O")
else:
    print("Different number of X and O")

