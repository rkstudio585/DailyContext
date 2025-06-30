import os
from widgets.config import Config
from widgets.date_time import DateTimeWidget
from widgets.quote import QuoteWidget
from widgets.todo import TodoWidget
from widgets.til import TilWidget
from widgets.daily_question import DailyQuestionWidget

def main():
    config = Config()

    print("\n--- DailyContext Dashboard ---")

    date_time_widget = DateTimeWidget(config)
    date_time_widget.display()

    quote_widget = QuoteWidget(config)
    quote_widget.display()

    todo_widget = TodoWidget(config)
    todo_widget.display()

    til_widget = TilWidget(config)
    til_widget.display()

    daily_question_widget = DailyQuestionWidget(config)
    daily_question_widget.display()

    print("------------------------------\n")

if __name__ == "__main__":
    main()