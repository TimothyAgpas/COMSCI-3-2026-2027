
def greet_students(name, nChar):
    for i in range(min(nChar, len(name))):
        print(name[i])


print("===== CODE #1 =====")

name = input("Enter a Name: ")
nChar = input("Enter any numeric number: ")
nChar = int(nChar)

greet_students(name, nChar)


def inverted_triangle(name, nChar):
    for i in range(nChar, 0, -1):
        print(name[0:i])


print("\n===== CODE #2 =====")

name = input("Enter a Name: ")

inverted_triangle(name, len(name))


def sum_of_squared(n):
    total = 0

    for i in range(1, n + 1):
        total += i ** 2

    return total


print("\n===== CODE #3 =====")

n = 0

while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100: ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))
