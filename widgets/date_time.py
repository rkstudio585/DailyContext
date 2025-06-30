from datetime import datetime
from rich.panel import Panel
from rich.text import Text

class DateTimeWidget:
    """A widget to display the current date and time."""
    def __init__(self):
        """Initializes the DateTimeWidget."""
        pass

    def get_content(self):
        """Generates a panel with the current date and time."""
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        time_str = now.strftime("%I:%M:%S %p")
        
        text = Text(f"{date_str}\n{time_str}", justify="center")
        return Panel(text, title="Date & Time", border_style="green")