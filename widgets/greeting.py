from datetime import datetime
from widgets.base_widget import Widget

class GreetingWidget(Widget):
    def display(self):
        if not self.config.get('greeting', {}).get('enabled', False):
            return

        name = self.config.get('greeting', {}).get('name', 'User')
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            greeting = "Good morning"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        print(f"{greeting}, {name}!")
