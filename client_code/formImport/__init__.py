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
    # Check if a file is selected
    if file:
      # Validate file type
      if file.name.lower().endswith('.csv'):
        self.uploaded_file = file
        print("File uploaded:", self.uploaded_file.name)  # Debugging line
      else:
        # Inform user that the file type is not supported
        alert("Please upload a CSV file.")
        self.uploaded_file = None  # Clear the uploaded file
    else:
      print("No file selected.")  # Debugging line

  def process_button_click(self, **event_args):
    print("Process button clicked")  # Debugging line
    if self.uploaded_file:
      try:
        # Call the server function and pass the stored file object
        result = anvil.server.call('process_csv', self.uploaded_file)
        print("Result from server:", result)  # Debugging line
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

