# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own.


# number = input("Enter a number:")
# num = int(number)
#
# if num % 15 ==0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(number)

def fizz_buzz(num):
    if not num%15:
        return 'FizzBuzz'
    if not num%3:
        return 'Fizz'
    if not num%5:
        return 'Buzz'
    return str(num)


num = input("Enter a number: ")

fizz_buzz(num)

