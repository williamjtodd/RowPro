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
        self.uploaded_file = None  # Initialize a variable to store the file
        self.load_workouts()  # Load workout data when the form initializes

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
                
                # Update text labels with workout details
                workout_number = 1
                for workout_name, details in result.items():
                    # Construct the label name
                    label_name = f'lblWorkout{workout_number}'
                    if hasattr(self, label_name):
                        label = getattr(self, label_name)
                        # Format details into a string for display
                        details_text = f"Workout {workout_number}\n" + '\n'.join([f"{k}: {v}" for k, v in details.items()])
                        label.text = details_text
                    else:
                        print(f"Label {label_name} not found.")
                    workout_number += 1
            
            except Exception as e:
                print("Error processing file:", e)  # Debugging line
        else:
            print("No file uploaded.")
    
    def load_workouts(self):
      try:
        result = anvil.server.call('get_user_workouts')
        if result.get('status') == 'success':
            # Update text labels with workout details
            workout_number = 1
            for workout_name, details in result.items():
                if workout_name == 'status':
                    continue  # Skip the status field
                
                # Construct the label name
                label_name = f'lblWorkout{workout_number}'
                if hasattr(self, label_name):
                    label = getattr(self, label_name)
                    # Format details into a string for display
                    details_text = f"{workout_name}\n" + '\n'.join([f"{k}: {v}" for k, v in details.items()])
                    label.text = details_text
                else:
                    print(f"Label {label_name} not found.")
                workout_number += 1
        else:
            alert(f"Error loading workouts: {result.get('message', 'Unknown error')}")
      except Exception as e:
        alert(f"Error loading workouts: {str(e)}")


    def btnDashboard_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('formDashboard')

    def btnProfile_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('formProfile')
