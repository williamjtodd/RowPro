from ._anvil_designer import formImportTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class formImport(formImportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnDashboard_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('formDashboard')
    pass

  def btnProfile_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('formProfile')
    pass
