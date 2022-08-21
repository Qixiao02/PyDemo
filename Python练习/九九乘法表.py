for i in range(1, 3):
    for j in range(1, i + 1):
        print('%d*%d = %d' % (i, j, i * j), end='\t')
    print()
