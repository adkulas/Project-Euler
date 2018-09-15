def ispalendrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def largest_palendrome(digits):
    max_num = 10**(digits)-1
    for i in range(max_num, 1, -1):
        for j in range(max_num, 1, -1):
            if ispalendrome(i*j):
                return i, j

if __name__ == '__main__':
    i, j = largest_palendrome(3)
    print(i,j, i*j)