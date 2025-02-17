from sympy import isprime

def get_sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 2
    else:
        return 3

def for_loop():
    list = []
    c = 0
    for i in range(50):
        if c < 10 and isprime(i):
            c = c + 1
            list.append(i)
    return list        

def while_loop():
    i = 0
    sum = 0
    while i < 100:
        i = i + 1
        sum = sum + i 
    return sum         
