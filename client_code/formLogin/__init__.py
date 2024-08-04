from ._anvil_designer import formLoginTemplate
from anvil import *
import anvil.server

class formLogin(formLoginTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)

    def btnLogIn_click(self, **event_args):
        email = self.tbEmail.text
        password = self.tbPassword.text
        result = anvil.server.call('login_user', email, password)
        if result['status'] == 'success':
            Notification("Login successful", timeout=2).show()
            open_form('formProfile')
        else:
            alert(result['message'])

    def btnSignUp_click(self, **event_args):
        email = self.tbEmail.text
        password = self.tbPassword.text
        if not email or not password:
            alert("Please fill in all fields.")
            return

        confirm_password_box = TextBox(type="password")
        confirm_password = alert(content=confirm_password_box, title="Confirm Password", buttons=[("OK", True), ("Cancel", False)])
        
        if not confirm_password:
            return

        if confirm_password_box.text != password:
            alert("Passwords do not match.")
            return

        result = anvil.server.call('sign_up_user', email, password)
        if result['status'] == 'success':
            Notification("Sign-up successful", timeout=2).show()
            open_form('formProfile')
        else:
            alert(result['message'])

    def btnClose_click(self, **event_args):
        open_form('formLogin.formGoBack')
