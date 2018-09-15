def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primefactorizer(num):
    for i in range(2,num):
        if isprime(i):
            if num % i == 0:
                primefactors.add(int(i))
                primefactorizer(int(num/i))
    return num

def factorizer(num):
    for i in range(2,num):
        if num % i == 0:
            regfactors.append(int(i))
            print(int(num/i), i)
            factorizer(int(num/i))
            return i
    return regfactors.append(int(num))

num1 = 40575
num2 = 600851475143
regfactors = []
factorizer(num1)
print(sorted(set(regfactors)))
primefactors = set([])
primefactorizer(num1)
print(sorted(primefactors))