import getpass
from ..service.user import save_new_user


def create_admin():
    """Creates the admin user."""
    email = input("Enter email address: ")
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter password again: ")
    if password != confirm_password:
        print("Passwords don't match")
    else:
        try:
            save_new_user(
                {
                    "email": email,
                    "password": password,
                    "username": email,
                    "is_admin": True,
                }
            )
            print(f"Admin with email {email} created successfully!")
        except Exception:
            print("Couldn't create admin user.")
