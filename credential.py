class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []

    def __init__(self,account_email,username,password):

        self.account_email = account_email
        self.username = username
        self.password = password

    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''
 
        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)