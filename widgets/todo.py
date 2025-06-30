from rich.panel import Panel
from rich.text import Text

class TodoWidget:
    def __init__(self, config):
        self.config = config

    def get_content(self):
        try:
            with open(self.config['paths']['todo'], 'r') as f:
                tasks = f.readlines()
            
            if not tasks:
                text = Text("No tasks found.", justify="center")
            else:
                task_list = "".join([f"- [ ] {task.strip()}\n" for task in tasks])
                text = Text(task_list)

            return Panel(text, title="To-Do List", border_style="cyan")
        except FileNotFoundError:
            return Panel(Text("todo.txt not found.", justify="center"), title="To-Do List", border_style="red")
