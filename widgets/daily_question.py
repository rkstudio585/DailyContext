from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

class DailyQuestionWidget:
    def __init__(self, config):
        self.config = config
        self.questions = [
            "What are you grateful for today?",
            "What is one thing you want to accomplish today?",
            "What is something that made you smile today?",
            "How are you feeling today, and why?",
            "What is one new thing you learned today?"
        ]

    def get_content(self):
        import random
        question = random.choice(self.questions)
        panel = Panel(Text(question, justify="center"), title="Daily Question", border_style="blue")
        return panel

    def ask_question(self, console):
        answer = Prompt.ask("[bold blue]Your Answer[/bold blue]")
        self.log_answer(answer)

    def log_answer(self, answer):
        log_file = self.config['paths']['daily_log']
        from datetime import datetime
        date_str = datetime.now().strftime("%Y-%m-%d")
        with open(log_file, 'a') as f:
            f.write(f"## {date_str}\n\n**Question:** {self.get_content().renderable.plain}\n\n**Answer:** {answer}\n\n")
