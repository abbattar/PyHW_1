my_text = 'ааАббБввВ gtyuj а 6& В -aа-- вббваб фывВБво шелабВи Пр%АбВ зкуст'
print(my_text)

my_text = ' '.join(filter(lambda x: not ('а' in x and 'в' in x and 'б' in x),
                          my_text.lower().split()))
print(my_text)