# import sys
# sys.setrecursionlimit(10000)

# def factorial(n):
#     print(n)
#     return n * factorial(n-1)

# def factorial(n):
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)

# making sure the function stops for every arg

def factorial(n):
    assert n >= 0 and int(n) == n, 'the number must be positive only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

factorial(3) 

# ---------------------------fibonacci ------------------
# step 1
# def fib(n):
#     return fib(n-1) + fib(n-2)

# step 2
# def fib(n):
#     if n in [0,1]:
#         return n 
#     else:
#         return fib(n-1) + fib(n-2)

# step 4
def fib(n):
    assert n >= 0 and int(n) == n , 'the number must be positive only'
    if n in [0,1]:
        return n 
    else:
        return fib(n-1) + fib(n-2)


fib(10)

def findNumber(n):
    assert n >=0 and int(n), 'please enter postive number only '
    if n == 0:
        return 0
    else:
        return int(n%10) + findNumber(int(n/10))

findNumber(8)
    
# step 2
# def power(base, exp):
#     return base * power(base, exp-1)
# # step 2
# def power(base, exp):
#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     else:
#         return base * power(base, exp-1)

def power(base, exp):
    assert exp >= base and int(exp), 'please enter positive number only'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

power(2,4)

def gCD(a,b):
    assert int(a) == a and int(b) == b, 'the number must be integer only'
    if a <0:
        a = - 1 * a 
    if b < 0:
        b = -1 * b 
    if b == 0:
        return a 
    else:
        return gCD(b, a%b)


gCD(26, 28)

def dec2bin(n):
    assert int(n) == n, 'the paramter must be integer only'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * dec2bin(int(n/2))

dec2bin(25)
