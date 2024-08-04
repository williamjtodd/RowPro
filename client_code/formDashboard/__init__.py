from ._anvil_designer import formDashboardTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class formDashboard(formDashboardTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Initialize plot type
        self.plot_type = 'bar'  # Default to bar graph
        self.update_plot()  # Initial plot update

    def update_plot(self):
        """Update the plot with data from the server and the current plot type."""
        try:
            result = anvil.server.call('get_workout_data')
            x = [row['StrokeCount'] for row in result]
            y = [row['AvgWatts'] for row in result]

            if self.plot_type == 'bar':
                self.plot_1.data = [
                    go.Bar(
                        x=x,
                        y=y,
                        name='Stroke Count vs Avg Watts'
                    )
                ]
            elif self.plot_type == 'line':
                self.plot_1.data = [
                    go.Scatter(
                        x=x,
                        y=y,
                        mode='lines+markers',
                        name='Stroke Count vs Avg Watts'
                    )
                ]
            elif self.plot_type == 'scatter':
                self.plot_1.data = [
                    go.Scatter(
                        x=x,
                        y=y,
                        mode='markers',
                        name='Stroke Count vs Avg Watts'
                    )
                ]

            self.plot_1.layout = go.Layout(
                title='Workout Data',
                xaxis=dict(title='Stroke Count'),
                yaxis=dict(title='Avg Watts')
            )
        except Exception as e:
            alert(f"Error retrieving workout data: {str(e)}")

    def btnBarGraph_click(self, **event_args):
        """Show the bar graph."""
        self.plot_type = 'bar'
        self.update_plot()

    def btnLineGraph_click(self, **event_args):
        """Show the line graph."""
        self.plot_type = 'line'
        self.update_plot()

    def btnScatterPlot_click(self, **event_args):
        """Show the scatter plot."""
        self.plot_type = 'scatter'
        self.update_plot()

    def btnProfile_click(self, **event_args):
        """Navigate to profile form."""
        open_form('formProfile')

    def btnImport_click(self, **event_args):
        """Navigate to import form."""
        open_form('formImport')
