import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import pandas as pd
import io

@anvil.server.callable
def process_csv(file):
    try:
        # Convert StreamingMedia to a file-like object
        file_stream = io.BytesIO(file.get_bytes())
        # Load the file into a pandas DataFrame
        df = pd.read_csv(file_stream)
        
        # Convert 'Date' column to datetime format
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        else:
            return {"error": "Date column not found in the CSV file."}
        
        # Sort the DataFrame by the 'Date' column in descending order
        df_sorted = df.sort_values(by='Date', ascending=False)
        
        # Select specific columns
        columns_to_keep = ['Date', 'Work Distance', 'Stroke Rate/Cadence', 'Stroke Count', 'Avg Watts']
        if not all(col in df_sorted.columns for col in columns_to_keep):
            return {"error": "One or more required columns are missing from the CSV file."}
        
        df_filtered = df_sorted[columns_to_keep]
        
        # Get the most recent records
        num_recent_records = 5  # Number of recent records to retrieve
        df_recent = df_filtered.head(num_recent_records)
        
        # Convert DataFrame to a dictionary with named keys
        result = {}
        for i, row in df_recent.iterrows():
            record_name = f'Workout {i + 1}'
            result[record_name] = row.to_dict()
        
        return result
        
    except Exception as e:
        return {"error": str(e)}  # Return error details if something goes wrong

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
