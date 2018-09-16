"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# Reduce the problem from 3 unknowns to 2 unknowns using substitution
# 3. 2ab + 2000a + 2000b = 1000000
# 3. x (1/a) -> 2b + 2000 + 2000b/a = 1000000 /a
# solve for b 3. -> b = 1000 * (500 - a)/(a+1000)


def solve_for_b_c(a):
    b = 1000 * (500 - a)/(a+1000)
    c = 1000 - a - b
    return b, c

def is_natural(num):
    return num % 1 == 0

if __name__ == '__main__':
    # b must return a natural number
    # loop through all possible a and check if b is natural
    for a in range(1,1000):
        b, c = solve_for_b_c(a)
        if is_natural(b):
            break
    print(f'The value of a is {a}, b is {b} and c is {c}')
    print(f'The product of abc is {a*b*c}')

