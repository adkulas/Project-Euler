def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def factorizer(num):
    for i in range(2,num):
        if num % i == 0:
            factors.append(int(i))
            print(int(num/i), i)
            factorizer(int(num/i))
            return i
    return factors.append(int(num))

num1 = 13195
num2 = 600851475143
factors = []
factorizer(num1)
print(sorted(set(factors)))