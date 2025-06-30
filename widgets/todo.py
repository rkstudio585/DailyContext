"""Widget to display a to-do list.

This widget reads tasks from a text file and displays them as a checklist.
It supports Markdown-style checklists (`- [ ]` and `- [x]`).
"""

from rich.panel import Panel
from rich.text import Text

class TodoWidget:
    """A widget to display a to-do list."""
    def __init__(self, config):
        """Initializes the TodoWidget with configuration."""
        self.config = config

    def get_content(self):
        """Generates a panel with the to-do list."""
        try:
            with open(self.config['paths']['todo'], 'r') as f:
                tasks = f.readlines()
            
            if not tasks:
                text = Text("No tasks found.", justify="center")
            else:
                task_list = ""
                for task in tasks:
                    task = task.strip()
                    if task.startswith("- [x]"):
                        task_list += f"[s green]{task}[/s green]\n"
                    elif task.startswith("- [ ]"):
                        task_list += f"[bold red]{task}[/bold red]\n"
                    else:
                        task_list += f"- [ ] {task}\n"
                text = Text.from_markup(task_list)

            return Panel(text, title="To-Do List", border_style="cyan")
        except FileNotFoundError:
            return Panel(Text("todo.txt not found.", justify="center"), title="To-Do List", border_style="red")