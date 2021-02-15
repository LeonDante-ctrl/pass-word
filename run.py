from user import User
from credentials import Credential
import random
import string

dash = '-' * 60


def create_account(account_name, username, password, confirm_password):
    """
    function to create a new account
    """

    new_user = User(account_name, username, password, confirm_password)

    return new_user


def save_details(user):
    """
    function to save save_details
    """
    user.save_detail()


def display_all_details():
    """
    function used to return all saved save_details
    """
    return User.display_all_details()


def check_existing_user(username):
    """
    a function that is used to check and return all existing accounts
    """

    return User.user_exist(username)
