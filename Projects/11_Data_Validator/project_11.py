import json
#========== 1. LOAD USERS FUNCTION ============
def load_users():
    try:
        with open("11_Data_Validator/users.json", "r") as data:
            users = json.load(data)
            return users
    except FileNotFoundError:
        print("File not found, Kindly check file path or file existance !")

#========== 2. ID VALIDATION FUNCTION ============
def id_validation(i):
    try:
        str_id = str(i).strip()
        if not str_id:
            return False, str_id, "ID is empty"
        elif not str_id.isdigit():
            return False, str_id, "ID is not digit"
        num_id = int(str_id)
        if not num_id > 0:
            return False,num_id, "ID is <= 0"
        else:
            return True,num_id, "Valid ID"
    except:
        return False, i, "ID does not exits"

#========== 3. NAME VALIDATION FUNCTION ============
def name_validation(users):
    valid_names = []
    invalid_names = []
    for user in users:
        n = user.get('name', '')
        user_id = user.get('id', 'N/A')
        try:
            name = str(n).strip()
            if not name:
                is_valid, msg = False, "Name is empty"
            elif not name.replace(" ", "").isalpha():
                is_valid, msg = False, "Name is not Alphabet"
            else:
                is_valid, msg = True, "Valid Name"
        except:
            is_valid, msg = False, "Name does not exits"
        record = {
        'id' : user_id,
        'name' : n,
        'message' : msg
        }
        if is_valid:
                valid_names.append(record)
        else:
                invalid_names.append(record)
    return valid_names, invalid_names


#========== 4. AGE VALIDATION FUNCTION ============
def age_validation(users):
    valid_ages = []
    invalid_ages = []
    for user in users:
        a = user.get('age', '')
        user_id = user.get('id', 'N/A')
        try:
            str_age = str(a).strip()
            if not str_age:
                is_valid, msg = False,  "Age is empty"
            elif not str_age.isdigit():
                is_valid, msg = False,  "Age is not digit"
            num_id = int(str_age)
            if not num_id > 0:
                is_valid, msg = False,  "Age is <= 0"
            else:
                is_valid, msg = True,  "Valid Age"
        except:
            is_valid, msg = False,  "Age does not exits"
        record = {
        'id' : user_id,
        'name' : a,
        'message' : msg
        }
        if is_valid:
                valid_ages.append(record)
        else:
                invalid_ages.append(record)
    return valid_ages, invalid_ages

#========== 5. EMAIL VALIDATION FUNCTION ============
def email_validation(users):
    valid_emails = []
    invalid_emails = []
    for user in users:
        e = user.get('email', '')
        user_id = user.get('id', 'N/A')
        try:
            email = str(e).strip()
            if ("@" in email) and ("." in email):
                is_valid, msg = True, "Valid Email"
            else:
                 is_valid, msg = False, "Not Valid Email"
        except:
            is_valid, msg = False, "Email does not exits"
        record = {
        'id' : user_id,
        'name' : e,
        'message' : msg
        }
        if is_valid:
                valid_emails.append(record)
        else:
                invalid_emails.append(record)
    return valid_emails, invalid_emails

#================= MAIN ==============
users = load_users()

#-------------- ID VALIDATION -------
ids = []
for id in users:
    ids.append((id["id"]))

valid_ids = []
invalid_ids = []
for i in ids:
    is_valid, id, msg = id_validation(i)
    record = {
        'id' : id,
        'message' : msg
    }
    if is_valid:
        valid_ids.append(record)
    else:
        invalid_ids.append(record)





#-------------- FUNCTION CALLINGS  ----------
valid_names, invalid_names = name_validation(users)
valid_ages, invalid_ages = age_validation(users)
valid_emails, invalid_emails = email_validation(users)
#----------------------------------------------
#               IDS
#---------------------------------------------
def name_validation_2(i):
     valid_records = 0
     lists = valid_ids + valid_names + valid_ages + valid_emails
     for id in lists:
          if i == id['id']:
               valid_records += 1
     return valid_records
valid_records = 0            
for i in ids:
     valid_records += name_validation_2(i)




#============ FINAL REPORT =================
print("=" * 40)
print("         DATA VALIDATION REPORT         ")
print(f"{'=' * 40}\n")
all_records = valid_ids + invalid_ids + valid_names + invalid_names + valid_ages + invalid_ages + valid_emails + invalid_emails
print(f" Total Records: {len(all_records)}")
valid_records = valid_ids + valid_names + valid_ages + valid_emails 
print(f" Valid Records: {len(valid_records)}")
invalid_records =  invalid_ids +  invalid_names + invalid_ages   + invalid_emails
print(f" Invalid Records: {len(invalid_records)}\n")
print("- " * 20)
print("         INVALID RECORDS         ")
print(f'{"- " * 20}\n')

for record in invalid_records:
     print(f"ID: {record['id']}")
     print(f"Reason: {record['message']}\n")
print("=" * 40)



