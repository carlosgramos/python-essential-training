#!/user/bin/env python3

#The kwyword def defines a function, and it will always include parenthesis even if no 
#arguments are passed. Also, notice the use of a default argument.

def function(n = 0):
    print(n)
    
#A function must be called
function(47)

#All functions return a value
x = function()
print(x)

#Prime numbers are positive, and are bigger than 1, and it's factors are only 1 and itself
def is_prime(n):
    if n <= 1:
        return False
    for x in range (2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()        