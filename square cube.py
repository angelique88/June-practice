import math


def check_square_and_cube(lst):
    root = math.sqrt(lst[0])
    if root **3 != lst[1]:
        return False
    else:
        return True


lst = [4, 9]

print(check_square_and_cube(lst))


