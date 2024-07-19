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
    alert(result)
