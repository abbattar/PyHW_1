from tlph_clients import *

def user_bookmark(user_id):
    with open('user.csv', 'a') as file:
        file.write(f'{user_id} id name {get_name(user_id)} second_name {get_scnd_name(user_id)}\
 workplace {get_workplace(user_id)} birsday {get_brth_date(user_id)}\
 telephone_number {get_tlph_number(user_id)}\n')