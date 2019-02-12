#!/usr/bin/env python3.6
from credential import Credential

def create_credential(account_type,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_type,username,password)
    return new_credential
    
def save_credentials(credential): 
    ''' 
    Function to save credential
    '''
    credential.save_credential()

def del_credentials(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential() 

def find_credentials(credential):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_username(username)

def check_existing_credentials(username):
    '''
    Function that check if a ccredential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)  

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:

        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential,dl-delete credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New Credential")
                print("-"*10)

                print ("account_type....")
                account_type = input()

                print("username ...")
                username = input()

                print("password ...")
                password= input()
                save_credentials(create_credential(account_type,username,password)) # create and save new credential.
                print ('\n')
                print(f"New Credential {account_type,username,password}  created")
                print ('\n')

        elif short_code == 'dc':

            if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for credential in display_credentials():
                        print(f"{credential.account_type} {credential.username} .....{credential.password}")

                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == 'fc':

                print("Enter the password you want to search for")

                search_password = input()
                if check_existing_credentials(search_password):
                        search_credential = find_credential(search_password)
                        print(f"{search_credential.account_email} {search_credential.username}")
                        print('-' * 20)

                        print(f"Password.......{search_credential.password}")
                        print(f"Account_email.......{search_credential.account_email}")
                else:
                        print("That credential does not exist")

        elif short_code == 'dl':

                print("Enter the account_type you want to delete ")


                search_account_type = input()

                if check_existing_credentials(search_account_type):
                        search_credential = find_account_type(search_account_type)
                        
                        del_credentials(search_account_type) 
                        print("Credetial Delete")

                else:
                    print("Credential doesn't exist")


        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

        main()