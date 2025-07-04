"""Widget to display a daily question.

This widget selects a random question from a predefined list.
The answer is logged via the `reflect.py` script.
"""
import random
from rich.panel import Panel
from rich.text import Text

class DailyQuestionWidget:
    """A widget to display a daily question."""
    def __init__(self, config):
        """Initializes the DailyQuestionWidget with configuration."""
        self.config = config
        self.questions = [
            "What are you grateful for today?",
            "What is one thing you want to accomplish today?",
            "What is something that made you smile today?",
            "How are you feeling today, and why?",
            "What is one new thing I learned today?"
        ]
        self.question = random.choice(self.questions)

    def get_content(self):
        """Generates a panel with the daily question."""
        panel = Panel(Text(self.question, justify="center"), title="Daily Question", border_style="blue")
        return panel

    def log_answer(self, answer):
        """Logs the user's answer to the daily log file."""
        log_file = self.config['paths']['daily_log']
        from datetime import datetime
        date_str = datetime.now().strftime("%Y-%m-%d")
        with open(log_file, 'a') as f:
            f.write(f"## {date_str}\n\n**Question:** {self.question}\n\n**Answer:** {answer}\n\n")