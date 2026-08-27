import requests
URL = "https://dummyjson.com/users"

def fetch_user_data():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError as c:
        print(f"ERROR : {c}")
    except requests.exceptions.Timeout as t:
        print(f"ERROR : {t}")
    except requests.exceptions.HTTPError as h:
        print(f"ERROR : {h}")
    except requests.RequestException as r:
        print(f"ERROR : {r}")


def clean_user_data(users):
    clean_users = []
    for user in users:
        clean_user = {
            'id' : user.get('id', 'N/A'),
            'fName' : user.get('firstName', 'N/A'),
            'lName' : user.get('lastName', 'N/A'),
            'email' : user.get('email', 'N/A'),
            'age' : user.get('age', 'N/A'),
            'city' : user.get('address', {}).get('city', 'N/A'),
            'company' : user.get('company', {}).get('name', 'N/A')
        }
        clean_users.append(clean_user)
    return clean_users

    