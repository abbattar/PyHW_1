x = float(input('Введите некоторое дробное число: '))
d_pow = int(input('Введите степень округления (не более 10): '))
d = 1 / (10 ** d_pow)
print(f'x = {((x % 1 ) * d_pow) - ((x % 1 ) * d_pow) % 1}')