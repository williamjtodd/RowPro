from ._anvil_designer import formDashboardTemplate
from anvil import *
import anvil.users
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class formDashboard(formDashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  

  def btnProfile_click(self, **event_args):
    open_form('formProfile')
    pass

  def btnImport_click(self, **event_args):
    open_form('formImport')
    pass
    
