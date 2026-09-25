num=int(input())

if num%2==0:
    print(f'{num} - четное')
else:
    print(f'{num} - нечетное')

if num>0:
    print(f'{num} - положительное')
elif num<0:
    print(f'{num} - отрицательное')
else:
    print(f'{num} равно 0')

if num in range(10, 51):
    print(f'{num} принадлежит диапазону [10, 50]')
else:
    print(f'{num} не принадлежит диапазону [10, 50]')