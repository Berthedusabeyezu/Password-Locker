import pyperclip

class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []

    def __init__(self,account_type,username,password):

        self.account_type= account_type
        self.username = username
        self.password = password

    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''
 
        Credential.credential_list.append(self)

    def delete_credentials(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a credential that matches that password.

        Args:
            password: password to search for
        Returns :
            Credential of person that matches the password.
        '''

        for credential in cls.credential_list:
            if credential.password == password:
                return credential   

    @classmethod
    def credential_exist(cls,password):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
           password:password to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.password == password:
                    return True

        return False 

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list   

    # @classmethod
    # def copy_account_type(cls,username):
    #     credential_found = Credential.find_by_username(username)
    #     pyperclip.copy(credential_found.account_type)    

    