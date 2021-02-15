class Credentials:
    """
    Class that will generate new instances of credentials
    """

    credential_detail = []

    def __init__(self, login_credential):

        """
        the __init__method helps us define properties for our objects.
        """

        self.login_credential = login_credential

        """
        arguments for our __init__method will include the following.
        """

    @classmethod
    def display_all_details(cls):

        return cls.user_detail

    @classmethod
    def find_by_username(cls, username):

        for user in cls.user_detail:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):

        for user in cls.user_detail:
            if user.username == username:
                return True
