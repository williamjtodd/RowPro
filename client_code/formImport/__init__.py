from ._anvil_designer import formImportTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class formImport(formImportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.uploaded_file = None  # Initialize a variable to store the file


  def selectedCSVFile_change(self, file, **event_args):
    # Store the uploaded file
    if file:
      self.uploaded_file = file
      print("File uploaded:", self.uploaded_file.name)  # Debugging line

  def process_button_click(self, **event_args):
    if self.uploaded_file:
      # Call the server function and pass the stored file object
      try:
        result = anvil.server.call('process_csv', self.uploaded_file)
        print(result)
      except Exception as e:
        print("Error processing file:", e)  # Debugging line
      else:
        print("No file uploaded.")


  
  def btnDashboard_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('formDashboard')
    pass

  def btnProfile_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('formProfile')
    pass

