from datetime import datetime
from widgets.base_widget import Widget

class DateTimeWidget(Widget):
    def display(self):
        format_str = self.config.get('date_time', {}).get('format', '%Y-%m-%d %H:%M:%S')
        print(f"Date & Time: {datetime.now().strftime(format_str)}")
