print('     ',end='')
for k in range(1,10):
    print('{:<5}'.format(k),end="")
print('\n')
for i in range(1,10):
    print('{:<5}'.format(i),end="")
    for j in range(1,i+1):
        print('{:<5}'.format(i*j),end='')
    print('\n')

for i in range(1,10):
    for j in range(1,i+1): 
       print("%d*%d=%d"%(i,j,i*j),end=" ")
    print()

print ('\n'.join([' '.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))