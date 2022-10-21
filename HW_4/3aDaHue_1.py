x = float(input('Введите некоторое число: '))
d_pow = int(input('Введите степень округления (не более 10): '))
d = 1 / (10 ** d_pow)
def round_x(x, d_pow):
    y = (x - x % 1) + (((x % 1 ) * 10 ** d_pow) 
                       - ((x % 1 ) * 10 ** d_pow) % 1) * ( 1 / (10 ** d_pow))
    return y
str_int_x = str(round_x(x, d_pow)).split('.')[0]
str_decimal_x = str(round_x(x, d_pow)).split('.')[1]
len_x = len(str_int_x) + len(str_decimal_x[:d_pow + 1]) + 1     # + 1 из-за присутствия точки
# print(len_x)
print(str(round_x(x, d_pow + 1)).split('.')[1][d_pow:d_pow + 1])
print(str(round_x(x, d_pow))[:len_x] if 
      int(str(round_x(x, d_pow + 1)).split('.')[1][d_pow:d_pow + 1]) < 5
     else str(round_x(x, d_pow) + d)[:len_x])