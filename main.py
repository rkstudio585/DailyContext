"""Main script to run the DailyContext dashboard.

This script loads the configuration, initializes all the widgets,
and displays them in a structured layout using the rich library.
"""

import json
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

from widgets.date_time import DateTimeWidget
from widgets.quote import QuoteWidget
from widgets.todo import TodoWidget
from widgets.til import TILWidget
from widgets.daily_question import DailyQuestionWidget

def main():
    """Loads configuration, initializes widgets, and displays the dashboard."""
    # Load configuration from JSON file
    with open("config.json") as f:
        config = json.load(f)

    # Initialize Rich Console
    console = Console()

    # Create the main layout structure
    layout = Layout()
    layout.split(
        Layout(Panel("DailyContext", style="bold green"), name="header", size=3),
        Layout(ratio=1, name="main"),
        Layout(name="footer", size=5),
    )

    # Split the main layout into left and right columns
    layout["main"].split_row(Layout(name="left", ratio=2), Layout(name="right", ratio=3))
    
    # Split the right column for quote and to-do widgets
    layout["right"].split_column(Layout(name="quote"), Layout(name="todo"))

    # Initialize all widgets
    dt_widget = DateTimeWidget()
    quote_widget = QuoteWidget(config)
    todo_widget = TodoWidget(config)
    til_widget = TILWidget(config)
    dq_widget = DailyQuestionWidget(config)

    # --- Populate the layout with widget content ---
    layout["left"].update(dt_widget.get_content())
    layout["quote"].update(quote_widget.get_content())
    layout["todo"].update(todo_widget.get_content())
    layout["footer"].split_row(
        Layout(til_widget.get_content(), name="til"),
        Layout(dq_widget.get_content(), name="daily_question")
    )

    # Print the final layout to the console
    console.print(layout)

if __name__ == "__main__":
    main()