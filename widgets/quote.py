import requests
import json
from rich.panel import Panel
from rich.text import Text

class QuoteWidget:
    def __init__(self, config):
        self.config = config

    def get_content(self):
        try:
            response = requests.get(self.config['quote_api_url'])
            if response.status_code == 200:
                data = response.json()
                quote = data['content']
                author = data['author']
                text = Text(f'“{quote}”\n- {author}', justify="center")
                return Panel(text, title="Quote of the Day", border_style="magenta")
            else:
                return self.get_local_quote()
        except requests.exceptions.RequestException:
            return self.get_local_quote()

    def get_local_quote(self):
        try:
            with open(self.config['paths']['quotes'], 'r') as f:
                quotes = f.readlines()
            import random
            quote = random.choice(quotes).strip()
            text = Text(quote, justify="center")
            return Panel(text, title="Quote of the Day", border_style="magenta")
        except FileNotFoundError:
            return Panel(Text("Could not fetch a quote.", justify="center"), title="Quote of the Day", border_style="red")
