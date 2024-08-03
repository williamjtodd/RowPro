from ._anvil_designer import formProfileTemplate
from anvil import *
import anvil.server

class formProfile(formProfileTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)
        
        try:
            email = anvil.server.call('get_logged_in_user_email')
            if email:
                # Commenting out the problematic line
                # self.labelEmail.text = email
                
                # Alternative temporary display
                print(f"Logged in user's email: {email}")  # Print to console or use another method to display email
            else:
                Notification("No user logged in.", timeout=2).show()
        except anvil.server.NoServerFunctionError:
            alert("Server function 'get_logged_in_user_email' not found.")
        
    def btnDashboard_click(self, **event_args):
        open_form('formDashboard')
        
    def btnImport_click(self, **event_args):
        open_form('formImport')
