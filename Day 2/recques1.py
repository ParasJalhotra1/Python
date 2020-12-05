def rec(num):
    if num<=10:
        print(f'{num}', end=' ')
        rec(num+1)

rec(1)