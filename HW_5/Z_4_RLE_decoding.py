def rle_decode(data):
    decode = ''
    count = ''
    # for char in data:
    #     print(count, char, decode)
    #     if char.isdigit():
    #         count += char
    #     else:
    #         decode += char * int(count)
    #         count = ''
    # return decode
    for i in range(0, len(data), 2):
        count = int(data[i])
        decode += data[i+1]*count
    return decode

decoding_value = rle_decode('7a655 7f')    # Можно попрорсить пользователя ввести код
print('7a655 7f')
print(decoding_value)
