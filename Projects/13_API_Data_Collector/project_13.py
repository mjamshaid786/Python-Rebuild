# importing required library 
import requests # --> pip install requests
import json

API_URL = "https://dummyjson.com/users"
#=======================================
#       DATA FETCHING FUNCTION
#=======================================
def fetch_users():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Connection Error !")
    except requests.exceptions.Timeout:
        print("Time out error !")
    except requests.exceptions.HTTPError:
        print("HTTP Error !")
    except requests.RequestException as e: # for other errors
        print(f'Error: {e}')


#================================================
#      EXTRACTION REQUIRED DATA FUNCTION
#================================================

# Getting Required Fields From Use
def extract_user_data(users):
    clean_users = []
    for user in users:
        clean_user = {
            'id' : user['id'],
            'fname' : user['firstName'],
            'lname' : user['lastName'],
            'email' : user['email'],
            'age' : user['age'],
            'city' : user['address']['city'],
            'company' : user['company']['name']
        }
        clean_users.append(clean_user)

    return clean_users

#=======================================
#       SAVING DATA  FUNCTION
#=======================================

def save_to_json(clean_users):
    with open ("clean_users.json", 'w') as file:
        json.dump(clean_users, file, indent=4)



#=======================================
#       FUNCTION CALLING
#=======================================
data = fetch_users()
if data:
    users = data['users']
    clean_users = extract_user_data(users)
    save_to_json(clean_users)


    #=======================================
    #              FINAL REPORT
    #=======================================

    print("=" * 35)
    print("     API DATA COLLECTOR    ")
    print(f"{'=' * 35}\n")

    print(f"Users Fetched : {len(users)}")
    print(f"Users Saved : {len(clean_users)}")
    print(f"Output File : clean_users.json")

    print("\nData Collections Completed Successfully !")
    print("=" * 35)