from datetime import datetime
from rich.panel import Panel
from rich.text import Text

class DateTimeWidget:
    def __init__(self):
        pass

    def get_content(self):
        now = datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        time_str = now.strftime("%I:%M:%S %p")
        
        text = Text(f"{date_str}\n{time_str}", justify="center")
        return Panel(text, title="Date & Time", border_style="green")
