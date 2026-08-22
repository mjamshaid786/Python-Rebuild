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
        if not str_id.isdigit():
            return False, str_id, "ID is not digit"
        num_id = int(str_id)
        if not num_id > 0:
            return False,num_id, "ID is <= 0"
        else:
            return True,num_id, "Valid ID"
    except:
        return False, i, "ID does not exits"

#========== 3. NAME VALIDATION FUNCTION ============
def name_validation(n):
    try:
        name = n.strip()
        if not name:
            return False, name, "Name is empty"
        if not name.replace(" ", "").isalpha():
            return False, name, "Name is not Alphabet"
        else:
            return True, name, "Valid Name"
    except:
        return False, n, "Name does not exits"

#========== 4. AGE VALIDATION FUNCTION ============
def id_validation(i):
    try:
        str_id = str(i).strip()
        if not str_id:
            return False, str_id, "ID is empty"
        if not str_id.isdigit():
            return False, str_id, "ID is not digit"
        num_id = int(str_id)
        if not num_id > 0:
            return False,num_id, "ID is <= 0"
        else:
            return True,num_id, "Valid ID"
    except:
        return False, i, "ID does not exits"





#================= MAIN ==============
users = load_users()

#-------------- ID VALIDATION -------
# ids = []
# for id in users:
#     ids.append((id["id"]))

# valid_ids = []
# invalid_ids = []
# for i in ids:
#     is_valid, id, msg = id_validation(i)
#     record = {
#         'id' : id,
#         'message' : msg
#     }
#     if is_valid:
#         valid_ids.append(record)
#     else:
#         invalid_ids.append(record)
# print(f"valid :{valid_ids}")
# print(f"invalid :{invalid_ids}")
#-------------- NAME VALIDATION ----------
# names = []
# for name in users:
#     names.append(name['name'])
# valid_names = []
# invalid_names = []
# for n in names:
#     is_valid, name, msg = name_validation(n)
#     record = {
#         'name' : name,
#         'message' : msg
#     }
#     if is_valid:
#         valid_names.append(record)
#     else:
#         invalid_names.append(record)
# print(valid_names)
# print(invalid_names)
#-------------- AGE VALIDATION -----------
ages = []
for age in users:
    ages.append((id["age"]))

valid_ages = []
invalid_ages = []
for a in ages:
    is_valid, id, msg = id_validation(a)
    record = {
        'age' : age,
        'message' : msg
    }
    if is_valid:
        valid_ages.append(record)
    else:
        invalid_ages.append(record)
print(f"valid :{valid_ages}")
print(f"invalid :{invalid_ages}")