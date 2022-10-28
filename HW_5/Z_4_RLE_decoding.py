def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoding_value = rle_decode('6A1F2D7C1A17E')    # Можно попрорсить пользователя ввести код
print('6A1F2D7C1A17E')
print(decoding_value)
