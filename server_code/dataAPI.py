import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def sign_up_user(email, password):
    try:
        user = anvil.users.signup_with_email(email, password)
        if user:
            return {"status": "success"}
        else:
            return {"status": "error", "message": "Sign-up failed."}
    except anvil.users.UserExists:
        return {"status": "error", "message": "User already exists."}

@anvil.server.callable
def login_user(email, password):
    try:
        user = anvil.users.login_with_email(email, password)
        if user:
            return {"status": "success"}
        else:
            return {"status": "error", "message": "Login failed."}
    except anvil.users.AuthenticationFailed as e:
        if "confirmed your email address" in str(e):
            return {"status": "error", "message": "Please confirm your email address before logging in."}
        return {"status": "error", "message": f"Authentication failed: {str(e)}"}



@anvil.server.callable
def get_logged_in_user_email():
    user = anvil.users.get_user()
    if user:
        return user['email']
    else:
        return None

@anvil.server.callable
def update_profile(name, age):
    user = anvil.users.get_user()
    if user:
        user['name'] = name
        user['age'] = age
        return {"status": "success"}
    else:
        return {"status": "error", "message": "User not logged in."}