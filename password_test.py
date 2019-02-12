import unittest # Importing the unittest module
from password import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Bona","Kiki","bonkiki1","bonki2") # create user object
   

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Bona")
        self.assertEqual(self.new_user.last_name,"Kiki")
        self.assertEqual(self.new_user.username,"bonkiki1")
        self.assertEqual(self.new_user.password,"bonki2")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),6)
    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("Bona","Kiki","bonkiki2","bonki2") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),5)
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Bona","Kiki","bonkiki3","bonki2") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1) 

    # @classmethod
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("Bona","Kiki","bonkiki4","bonki2") # new user
        test_user.save_user()

        found_user = User.find_user_by_username("bonkiki4")

        self.assertEqual(found_user.password,test_user.password)
if __name__ == '__main__':
    unittest.main() 