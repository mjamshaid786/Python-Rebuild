from project_14 import fetch_user_data, clean_user_data
from project_14A import final_users_data
from project_14B import save_to_csv



#========== FUNCTION CALLINGS ============
data = fetch_user_data()
if data:
    users = data['users']
    clean_users = clean_user_data(users)
    final_users = final_users_data(clean_users)
    save_to_csv(final_users)

    #========== FINAL REPORT ============
    print('=' * 40)
    print("         API --> CSV PIPELINE     ")
    print(f"{'=' * 40}\n")

    print(f"Users Fetched: {len(users)}")
    print(f"Users Transformed: {len(final_users)}")
    print(f"Rows Saved: {len(final_users)}")
    print(f"Output File: final_users_data.csv\n")
    print(f"Pipeline Completed Successfully !\n")
    print('=' * 40)



