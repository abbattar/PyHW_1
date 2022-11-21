import data_base as d_b

def user_view(user, user_id):
    user = d_b.user_bookmark(user_id)
    return user