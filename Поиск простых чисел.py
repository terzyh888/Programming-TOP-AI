n=int(input())
def deliteli(x):
    delit = []
    for d in range(2, int(x**0.5)+1):
        if x%d==0:
            delit.append(d)
            delit.append(x//d)
    return delit

total=[]
for i in range(2, n+1):
    dividers=deliteli(i)
    if len(dividers)==0:
        total.append(i)

print(f'Список простых чисел:{total}')