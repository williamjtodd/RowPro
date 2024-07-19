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
    # Fetch the customer details by name
    row = app_tables.tblauthentication.get(IDAuth=IDAuth)
    if row:
        return {
            "IDAuth": row['IDAuth'],
            "Email": row['Email'],
            "Password": row['Password']
        }
    else:
        return None


'''SETTERS'''
@anvil.server.callable
def setAuthentication(IDAuth, email, password):
  # Generate a unique bill reference number
    existing_rows = list(app_tables.tblauthentication.search(tables.order_by("IDAuth", ascending=False)))
    if existing_rows:
        last_bill_ref = existing_rows[0]['IDAuth']
        new_bill_ref = int(last_bill_ref) + 1
    else:
        new_bill_ref = 1

    # Add a new row to the table `tbluserdetails`
    app_tables.tblauthentication.add_row(
        IDAuth=str(new_bill_ref).zfill(8),  # Ensure 8-digit Bill Reference Number. The reference number could be more complex, but there is no point. 
        Email=email,
        Password=password,
    )
    return "Created new customer record."