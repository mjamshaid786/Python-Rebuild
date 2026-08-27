from project_14 import clean_user_data
def final_users_data(clean_users):
    final_users = []
    for user in clean_users:
        final_user = {
            'id' : user['id'],
            'fName' : user['fName'] + ' ' + user['lName'],
            'email' : user['email'],
            'age' : user['age'],
            'city' : user['city'],
            'company' : user['company']

        }
        final_users.append(final_user)
    return final_users
