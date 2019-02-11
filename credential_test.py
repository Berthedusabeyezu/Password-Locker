import unittest # Importing the unittest module
from credential import Credential # Importing the user class
class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("James@gmail.com","jameso","kjames2") # create credetial object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_email,"James@gmail.com")
        self.assertEqual(self.new_credential.username,"jameso")
        self.assertEqual(self.new_credential.password,"kjames2")
        
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)
    

if __name__ == '__main__':
    unittest.main()