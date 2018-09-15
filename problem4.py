def ispalendrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def largest_palendrome(digits):
    max_num = 10**(digits)-1
    largest = 0
    for i in range(max_num, 1, -1):
        for j in range(max_num, 1, -1):
            print(i, j)
            if ispalendrome(i*j):
                if i*j > largest:
                    largest = i*j
    return largest

if __name__ == '__main__':
    print(largest_palendrome(3))