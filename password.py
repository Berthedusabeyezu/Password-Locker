class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def __init__(self,first_name,last_name,username,password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''
 
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 
    
    @classmethod
    def find_user_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username.

        Args:
            username: username to search for
        Returns :
            User of person that matches the username.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user      

   
   