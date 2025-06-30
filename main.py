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
    with open("config.json") as f:
        config = json.load(f)

    console = Console()

    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(ratio=1, name="main"),
        Layout(size=10, name="footer"),
    )

    layout["main"].split_row(Layout(name="left"), Layout(name="right"))
    layout["right"].split_column(Layout(name="top"), Layout(name="bottom"))

    dt_widget = DateTimeWidget()
    quote_widget = QuoteWidget(config)
    todo_widget = TodoWidget(config)
    til_widget = TILWidget(config)
    dq_widget = DailyQuestionWidget(config)

    layout["header"].update(Panel("DailyContext Dashboard", style="bold green"))
    layout["left"].update(dt_widget.get_content())
    layout["right"]["top"].update(quote_widget.get_content())
    layout["right"]["bottom"].update(todo_widget.get_content())
    layout["footer"].update(til_widget.get_content())

    console.print(layout)

    console.print(dq_widget.get_content())

if __name__ == "__main__":
    main()
