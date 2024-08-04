import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import pandas as pd

@anvil.server.callable
def process_csv(file):
    # Load the file into a pandas DataFrame
    df = pd.read_csv(file)
    # Perform operations on the DataFrame
    return df.head().to_dict()  # For example, return the first few rows

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
    except anvil.users.AuthenticationFailed:
        return {"status": "error", "message": "Invalid email or password."}

@anvil.server.callable
def get_user_profile():
    try:
        user = anvil.users.get_user()
        if user:
            profile = app_tables.tbluserelements.get(user_id=user)
            if profile:
                return {"status": "success", "name": profile['name'], "age": profile['age'], "pfp": profile['pfp']}
            else:
                return {"status": "error", "message": "Profile not found."}
        else:
            return {"status": "error", "message": "No user logged in."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@anvil.server.callable
def update_user_profile(name, age, pfp):
    try:
        user = anvil.users.get_user()
        if user:
            profile = app_tables.tbluserelements.get(user_id=user)
            if profile:
                profile['name'] = name
                profile['age'] = age
                profile['pfp'] = pfp
            else:
                app_tables.tbluserelements.add_row(user_id=user, name=name, age=age, pfp=pfp)
            return {"status": "success"}
        else:
            return {"status": "error", "message": "No user logged in."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
