"""Widget to display a random quote.

This widget fetches a random quote from an API and falls back to a local
file if the API is unavailable.
"""
import requests
import json
import random
from rich.panel import Panel
from rich.text import Text

class QuoteWidget:
    """A widget to display a random quote."""
    def __init__(self, config):
        """Initializes the QuoteWidget with configuration."""
        self.config = config

    def get_content(self):
        """Fetches a quote and returns it in a panel."""
        try:
            response = requests.get(self.config['quote_api_url'])
            if response.status_code == 200:
                data = response.json()
                quote = data['content']
                author = data['author']
                text = Text(f'"{quote}"\n- {author}', justify="center")
                return Panel(text, title="Quote of the Day", border_style="magenta")
            else:
                return self.get_local_quote()
        except requests.exceptions.RequestException:
            return self.get_local_quote()

    def get_local_quote(self):
        """Fetches a random quote from the local quotes file."""
        try:
            with open(self.config['paths']['quotes'], 'r') as f:
                quotes = f.readlines()
            if not quotes:
                return Panel(Text("Could not fetch a quote and no local quotes found.", justify="center"), title="Quote of the Day", border_style="red")
            quote = random.choice(quotes).strip()
            text = Text(quote, justify="center")
            return Panel(text, title="Quote of the Day", border_style="magenta")
        except FileNotFoundError:
            return Panel(Text("Could not fetch a quote.", justify="center"), title="Quote of the Day", border_style="red")