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
        self.new_user = User("Bona","Kiki","bonkiki","bonki2") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Bona")
        self.assertEqual(self.new_user.last_name,"Kiki")
        self.assertEqual(self.new_user.username,"bonki")
        self.assertEqual(self.new_user.password,"bonki2")


if __name__ == '__main__':
    unittest.main()