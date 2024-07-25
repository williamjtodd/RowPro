from ._anvil_designer import formLoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class formLogin(formLoginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def btnSignUp_click(self, **event_args):
        """This method is called when the button is clicked"""
        email = self.tbEmail.text
        password = self.tbPassword.text
        result = anvil.server.call("setAuthentication", email, password)
        anvil.server.call('setUserElements', email, password)
        alert(result)

    def btnLogIn_click(self, **event_args):
        """This method is called when the button is clicked"""
        print("btnLogIn_click method called")
        alert("Attempting to log in...")  # Test alert
        email = self.tbEmail.text
        password = self.tbPassword.text
        print(f"Email: {email}, Password: {password}")
        is_authenticated = anvil.server.call("checkCredentials", email, password)
        print(f"Authenticated: {is_authenticated}")
        if is_authenticated:
            print("Opening formDashboard...") 
            open_form('formDashboard')# Ensure it opens the form correctly
        else:
            print("Invalid credentials")
            alert("Invalid email or password. Please try again.")

    def btnClose_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('formLogin.formGoBack')
      pass
