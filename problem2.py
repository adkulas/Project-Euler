seq = []
sum = 0
while True:
    if len(seq) < 2:
        val = 1
    else:
        val = seq[-1] + seq[-2]
        if val > 4000000:
            break
    seq.append(val)
    if val % 2 == 0:
        sum += val

print(seq[-10:])
print(sum)