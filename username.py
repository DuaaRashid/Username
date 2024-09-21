# # 5-10. Checking Usernames:
print(f'\tUsername checking system')
curr_users : list[str] = ["faizan","duaa","samia","hamna","hiba"]
def main():
     while True:
          new_name=input(f"To quit the program, type 'y'\nEnter new username: ").lower()
          if new_name=="y":
               print("Exiting the program.")
               break
          if new_name in curr_users:
               print("Username already exists. Please choose another one.")
          else:
               print("Username available")
               create_account=input("Would you like to create this account? (y/n): ")
               if create_account=="y":
                    new_username=input("Enter your desired username: ").lower()
                    password=input("Enter a password: ")
                    curr_users.append(new_username)
                    print("Account Created Successfully")
               else:
                    print("Account creation aborted.")
main()