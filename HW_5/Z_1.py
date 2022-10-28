my_text = 'ааАббБввВ ваБВа а б В -абв-- вббваб фывВБво шелабВи Пр%АбВ авб'
print(my_text)

my_text = ' '.join(filter(lambda x: 'абв' not in x, my_text.lower().split()))
print(my_text)