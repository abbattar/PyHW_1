def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for i in range(len(data) - 1):
        if data[i] == prev_char:
            count += 1
            if count == 9:
                encoding = append( str(count) + prev_char)
                count = 1

        elif count == 9:
            encoding += str(count) + prev_char
            count += 1
        else: count += 1
    else:
        encoding += str(count) + prev_char
    return encoding

encoding_value = rle_encode('aaaaaaa5555555555555     fffffff')   # Можно попрорсить пользователя ввести значение

print(encoding_value)