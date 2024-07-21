import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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

'''GETTERS'''
@anvil.server.callable
def getAuthentication(IDAuth):
    # Fetch the customer details by IDAuth
    row = app_tables.tblauthentication.get(IDAuth=IDAuth)
    if row:
        return {
            "IDAuth": row['IDAuth'],
            "Email": row['Email'],
            "Password": row['Password']
        }
    else:
        return None

@anvil.server.callable
def checkCredentials(email, password):
    # Fetch the user by email and check the password
    row = app_tables.tblauthentication.get(Email=email)
    if row and row['Password'] == password:
        return True
    else:
        return False

'''SETTERS'''
@anvil.server.callable
def setAuthentication(email, password):
    # Generate a unique IDAuth
    existing_rows = list(app_tables.tblauthentication.search(tables.order_by("IDAuth", ascending=False)))
    if existing_rows:
        last_id_auth = existing_rows[0]['IDAuth']
        new_id_auth = last_id_auth + 1
    else:
        new_id_auth = 1

    # Add a new row to the table `tblauthentication`
    app_tables.tblauthentication.add_row(
        IDAuth=new_id_auth,  # Ensure IDAuth is a number
        Email=email,
        Password=password,
    )
    return "Created new customer record."
