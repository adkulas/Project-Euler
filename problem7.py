'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isprime(num):
    if num % 2 == 0:
        return False
    for i in range(3,num, 2):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    i = 1
    length = 0
    while length < n:
        i += 1
        if isprime(i):
            length += 1
    return i

if __name__ == '__main__':
    print(find_nth_prime(6))
    print(find_nth_prime(10001))

'''
Performance results 
=======================
In [64]: %%timeit
    ...: %run problem7.py
    ...:

11.5 s ± 170 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
'''