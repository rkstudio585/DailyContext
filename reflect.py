"""Script to handle the interactive daily reflection.

This script prompts the user with the daily question and saves their answer.
"""
import json
from rich.console import Console
from rich.prompt import Prompt
from widgets.daily_question import DailyQuestionWidget

def main():
    """Loads configuration, prompts for reflection, and saves the answer."""
    with open("config.json") as f:
        config = json.load(f)

    console = Console()
    dq_widget = DailyQuestionWidget(config)

    console.print(dq_widget.get_content())
    answer = Prompt.ask("[bold blue]Your Answer[/bold blue]")
    dq_widget.log_answer(answer)
    console.print("[green]Your reflection has been saved.[/green]")

if __name__ == "__main__":
    main()