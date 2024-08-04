from ._anvil_designer import formProfileTemplate
from anvil import *
import anvil.server

class formProfile(formProfileTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)
        self.load_user_profile()
      

    def load_user_profile(self):
        try:
            result = anvil.server.call('get_user_profile')
            if result.get('status') == 'success':
                self.tbName.text = result.get('name', '')
                self.tbAge.text = str(result.get('age', ''))
                self.flPFP.file = result.get('pfp', '')
            else:
                alert(f"Error loading profile: {result.get('message', 'Unknown error')}")
        except Exception as e:
            alert(f"Error loading profile: {str(e)}")

    def btnSubmit_click(self, **event_args):
        name = self.tbName.text
        age_text = self.tbAge.text
        pfp = self.flPFP.file

        try:
            age = int(age_text)  # Convert age to integer
        except ValueError:
            alert("Please enter a valid age.")
            return

        try:
            result = anvil.server.call('update_user_profile', name, age, pfp)
            if result['status'] == 'success':
                Notification("Profile updated successfully.", timeout=2).show()
            else:
                alert(f"Error: {result.get('message', 'Unknown error')}")
        except Exception as e:
            alert(f"Error updating profile: {str(e)}")

    def btnDashboard_click(self, **event_args):
        open_form('formDashboard')
        
    def btnImport_click(self, **event_args):
        open_form('formImport')

    def btnLogout_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('formLogin')
      pass
