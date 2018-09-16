'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np

def sum_of_squares(numbers):
    a = np.array(numbers)**2
    return np.sum(a)

def square_of_sum(numbers):
    a = sum(numbers)
    return a**2

if __name__ == '__main__':
    num1 = list(range(1,11))
    num2 = list(range(1,101))

    print(square_of_sum(num1) - sum_of_squares(num1))
    print(square_of_sum(num2) - sum_of_squares(num2))