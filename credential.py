class Credential:
    """
    Class that generates new instances of credentials
    """
    credential_list = []

    def __init__(self,account_email,username,password):

        self.account_email = account_email
        self.username = username
        self.password = password