from ._anvil_designer import formProfileTemplate
from anvil import *
import anvil.server

class formProfile(formProfileTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)
        self.load_user_profile()  # Call this method to load the user profile

    def load_user_profile(self):
        try:
            result = anvil.server.call('get_user_profile')
            # Debugging output
            alert(f"Profile data received: {result}")
            if result.get('status') == 'success':
                # Update the text boxes with the user's profile data
                self.tbName.text = result.get('name', '')
                self.tbAge.text = str(result.get('age', ''))
            else:
                alert(f"Error loading profile: {result.get('message', 'Unknown error')}")
        except Exception as e:
            alert(f"Error loading profile: {str(e)}")

    def btnSubmit_click(self, **event_args):
        name = self.tbName.text
        age_text = self.tbAge.text

        # Basic debugging to confirm method execution
        alert("Submit button clicked!")
        
        # Debugging alerts
        alert(f"Name: {name}")
        alert(f"Age: {age_text}")

        try:
            age = int(age_text)  # Convert age to integer
        except ValueError:
            alert("Please enter a valid age.")
            return

        # Call the server function to update user profile
        try:
            result = anvil.server.call('update_user_profile', name, age)
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
