"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

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

def generate_primes(stop):
    # start with first 2 prime numbers
    primes = [2,3]
    # all primes are in form 6k +/- 1, start with 6 
    k = 6
    while k+1 < stop:
        k_low_not_prime_flag = False
        k_high_not_prime_flag = False
        for prime in primes:
            if prime > math.sqrt(k+1):
                if not k_low_not_prime_flag:
                    primes.append(k-1)
                if not k_high_not_prime_flag:
                    primes.append(k+1)
                break
            if (k-1) % prime == 0:
                k_low_not_prime_flag = True
            if (k+1) % prime == 0:
                k_high_not_prime_flag = True
        k += 6
    return primes
            

if __name__ == '__main__':
    primes = generate_primes(2000000)
    print(primes[-10:])
    print(sum(primes))