from collections import Counter

text=input().lower()

counts=Counter(text)

for symbol, count in counts.items():
    print(f'Символ {symbol}-{count}')

for symbol, count in counts.most_common(3):
    print(f'Символ {symbol}-{count}')