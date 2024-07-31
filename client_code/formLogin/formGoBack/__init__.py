from ._anvil_designer import formGoBackTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class formGoBack(formGoBackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnBackLogin_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('formLogin')
    pass
