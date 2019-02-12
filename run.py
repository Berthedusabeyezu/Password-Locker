#!/usr/bin/env python3.6
from credential import Credential

    def create_credential(account_email,username,password):
        '''
        Function to create a new credential
        '''
        new_credential = Credential(account_email,username,password)
        return new_credential
    
    def save_credentials(credential): 
        '''
        Function to save credential
        '''
        credential.save_credential()

    def del_credential(credential):
        '''
        Function to delete a credential
        '''
        credential.delete_credential()

    def find_credential(credential):
        '''
        Function that finds a credential by username and returns the credential
        '''
        return Credential.find_by_username(username)

    def check_existing_credentials(username):
        '''
        Function that check if a ccredential exists with that username and return a Boolean
        '''
        return Credential.credential_exist(username)     