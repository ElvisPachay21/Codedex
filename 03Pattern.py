rows = 4
num = 1
for i in range(rows):
    print(' ' * (rows - i - 1) + ' '.join(str(num + j) for j in range(i + 1)))
    num += i + 1