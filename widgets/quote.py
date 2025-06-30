import os
import random
from widgets.base_widget import Widget

class QuoteWidget(Widget):
    def display(self):
        source = self.config.get('quote', {}).get('source', 'local')
        if source == 'local':
            file_path = self.config.get('quote', {}).get('file_path')
            if file_path and os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    quotes = [line.strip() for line in f if line.strip()]
                if quotes:
                    print(f"Quote: {random.choice(quotes)}")
                else:
                    print("Quote: No quotes found.")
            else:
                print("Quote: Local quotes file not found.")
        else:
            print("Quote: API integration not implemented yet.")
