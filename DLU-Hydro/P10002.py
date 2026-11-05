from decimal import Decimal, ROUND_HALF_UP

a, b, c = input().split('-')
result = []
for x in (a, b, c):
    d = Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    result.append(f'{d:.2f}')
print(' '.join(result))