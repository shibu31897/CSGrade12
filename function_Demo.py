# Function make the code resusable

# syntax
# def functionName(parameters):

# scope of function
import random


def isPaymentSuccessFul():
    return random.randint(999, 999999)


# argument vs parameter


#*args --> unlimited postional arguments
def sum(*args):  # a,b are parameters

    return args[-1]

def sumP(a,b):
    print(f"Value of a {a} and value of b is {b}")
    return a+b

print(sum(1, 5,7,8,9,9,9,65,65))  # 1, 5 is called argument here

# sumP(a=6,c=99)

#**kwargs -> unlimited keyword arguments

def whatisDivisor(**kwargs):
    q = kwargs['quotient']
    d = kwargs['dividend']
    ds = kwargs['divisor']
    num = q + d/ds
    print(num)

whatisDivisor(quotient=3,dividend=5,divisor=55)  #{"quotient" : 3,}

#default argument -> in case no value provided take defualt value
#defualt argument is always should be right side of (_)
def sub(a,b=0):
    return a-b
a = "Harshit"
print(f"My name is {a}")
