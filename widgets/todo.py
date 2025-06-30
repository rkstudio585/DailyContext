import os
from widgets.base_widget import Widget

class TodoWidget(Widget):
    def display(self):
        file_path = self.config.get('todo', {}).get('file_path')
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                tasks = [line.strip() for line in f if line.strip()]
            print("To-Do List:")
            if tasks:
                for task in tasks:
                    print(f"- {task}")
            else:
                print("- No tasks found.")
        else:
            print("To-Do List: To-Do file not found.")
