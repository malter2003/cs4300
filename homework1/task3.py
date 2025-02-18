from sympy import isprime

# return with different symbolic number based on sign of input
def get_sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 2
    else:
        return 3

def for_loop():
    list = [] # list of the prime numbers that we will gather
    c = 0 # count of prime numbers, we want the first ten
    for i in range(50): # loop from 0 to 49 inclusive
        if c < 10 and isprime(i): # if natural number is prime and the count is less than 10
            c = c + 1 # iterate count
            list.append(i) # add to list of primes
    return list        

def while_loop():
    i = 0
    sum = 0
    while i < 100: # loop from 0 to 99 inclusive
        i = i + 1 # this being before the sum addition makes it effectively 1 to 100
        sum = sum + i 
    return sum         
