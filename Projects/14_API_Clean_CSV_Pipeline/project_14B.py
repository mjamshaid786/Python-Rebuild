from project_14A import final_users_data
import csv
def save_to_csv(final_users):
    field_names = ['id', 'fName', 'email', 'age', 'city', 'company']
    with open('final_users_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(final_users)
