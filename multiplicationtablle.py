for i in range(10):
    a = 1
    while a <= i:
        print("{}*{}={: <2}".format(a, i, i * a),end=' ')
        a += 1
    print('\t')

print ('\n'.join([' '.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))