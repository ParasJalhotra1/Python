num = int(input('Enter a number:'))
 
if num % 2 == 0:
    print('Even:', end='')
    for even in range(num,num+10,2):
         print( even, end=' ')
print('\nOdd:', end='')
for num in range(num+1,num+10,2):
    
    print( num, end=' ')

    
