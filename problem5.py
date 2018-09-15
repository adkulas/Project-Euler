def check_divisible(num, divisor_list):
    for i in divisor_list:
        if num % i != 0:
            return False
    return True

def lowest_common_multiple(top_num):
    num = top_num
    divisors = list(range(1,top_num+1))
    while not check_divisible(num, divisors):
        num += top_num
    
    return num

if __name__ == '__main__':
    print(lowest_common_multiple(20))
    