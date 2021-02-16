from getpass import getpass

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


def find_user(username):
    """
    the function is used check details from the saved save_details
    """

    return User.find_by_username(username)


def generatePassword(num):
    genpas = ''

    for n in range(num):
        x = random.randint(0, 94)
        genpas += string.printable[x]  # integer values only accepted

    return genpas


def main():
    print('{:_^5}'.format('REMAIN SECURE WITH LEONS PASSWORD MANAGER'))

    print('\n')

    print('{:_^20}'.format('login'))

    print('\n')

    print("Key in locker username")

    user_name = input().upper()

    print(f"Hello {user_name}, Behold!!!, your password manager")

    print('\n')

    while True:

        list: str = ('''
            1 - Register a new account
            2 - Display accounts
            3 - Find accounts
            4 - Exit the locker\n''')
        print(list)

        short_code = input().lower()

        if short_code == '1':

            print(f"{user_name} Fill in some input")

            print("-" * 10)

            print("User name")

            account_name = input()

            print('\n')

            print("Username")
            username = input()

            print('\n')

            print("Need a randomly generated password?")

            print("yes", "no")
            ans = input().lower()

            if ans == 'yes':

                print(generatePassword(10))

                save_details(create_account(account_name, username, password, confirm_password))

                print('\n')

                print(f"{user_name} {account_name} account of {username} created and password saved")

                print('\n')


            elif ans == 'no':

                password = getpass('password:')
                print("*********")

                confirm_password = getpass('confirm password:')
                print("*********")

                save_details(create_account(account_name, username, password, confirm_password))

                print('\n')

                print(dash)

                print(f"Hey {user_name}")
                print(f"Your account name is {account_name}.com")
                print(f"Your username is {username}")
                print("encrypted passwords can be viewed through the option 2 / 3")

                print(dash)

                print('\n')

                print(f"{user_name} what action do you want to perform?")

        elif short_code == '2':

            if display_all_details():

                print(f"{user_name} preview all the saved accounts")

                print('\n')

                for user in display_all_details():
                    print(dash)

                    print(f"Account is {user.account_name}.com")
                    print(f"Account username is {user.username}")
                    print(f"The account's password is {user.password} keep this private")

                    print(dash)

                    print('\n')

                    print(f"{user_name} what action do you want to perform?")

            else:

                print('\n')

                print(f" {user_name} nothing saved just yet")

                print('\n')

                print(f"{user_name} what action do you want to perform?")

        elif short_code == '3':

            print(f"{user_name} Search for username here")

            search_username = input()

            if check_existing_user(search_username):

                search_username = find_user(search_username)

                print(dash)

                print(f"Account is {search_username.account_name}.com")
                print(f"Account username is {search_username.username}")
                print(f"Account password is {search_username.password} keep password private")

                print(dash)

                print(f"{user_name} what action do you want to perform?")

            else:
                print(f"{user_name} does ot exist")

                print(f"{user_name} what action do you want to perform?")

        elif short_code == "4":

            print("Cheers.")

            break

        else:
            print("Illegible , try that again")

            print(f"{user_name} what action do you want to perform?")

    if __name__ == '__main__':
        main()
