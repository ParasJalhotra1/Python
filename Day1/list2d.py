rows = int(input('Enter number of rows: '))
columns = int(input('Enter number of columns: '))

list2 = []
list1 = []
print('Enter elements one by one: ')
for i in range(rows):
    for j in range(columns):
        list1.append(int(input()))
    list2.append(list1)
    list1 = []
for i in list2:
    for j in i:
        print(j, end=' ')
    print()