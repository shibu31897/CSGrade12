# split function
# str = "This-is-a-pycharm IDE"
#
# print(str.split("-"))


# def sayHello():
#     """
#     This function will return hello
#     this is an example of docstring
#     """
#
#     print("Hello")
#
# sayHello()

# dictionary
# hash table
dictionary = {1: "One", 2: "Two", 3: "Three"}

# print(dictionary.get(4)) #if key now found : throws None
#
#
# print(dictionary[4]) #if key now found : throws exception/error


# def max(a):
#     b = 0
#     for i in a:
#         if i > b:
#             b = i
#
#     print(b)
#
#
# max([1, 2,0, 3, 4, 5])

# functions with dictionary
def add(a,b,c):
    return a+b+c


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def div(a,b):
    return a/b

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
sign = operation["+"]
op = sign(1,4,4)
print(op)

# a = 5  # global variable


# def whatIsa():
#     global a
#     for i in range(6):
#         a += i
#     print(a)
#
#
# whatIsa()

