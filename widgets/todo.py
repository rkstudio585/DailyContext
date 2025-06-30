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
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
            else:
                print("- No tasks found.")
        else:
            print("To-Do List: To-Do file not found.")

    def _read_tasks(self):
        file_path = self.config.get('todo', {}).get('file_path')
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        return []

    def _write_tasks(self, tasks):
        file_path = self.config.get('todo', {}).get('file_path')
        if file_path:
            with open(file_path, 'w') as f:
                for task in tasks:
                    f.write(f"{task}\n")

    def add_task(self, task):
        tasks = self._read_tasks()
        tasks.append(task)
        self._write_tasks(tasks)
        print(f"Task '{task}' added.")

    def remove_task(self, task_number):
        tasks = self._read_tasks()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            self._write_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

    def mark_complete(self, task_number):
        tasks = self._read_tasks()
        if 0 < task_number <= len(tasks):
            task = tasks[task_number - 1]
            if not task.startswith('[x]'):
                tasks[task_number - 1] = f'[x] {task}'
                self._write_tasks(tasks)
                print(f"Task '{task}' marked as complete.")
            else:
                print(f"Task '{task}' is already complete.")
        else:
            print("Invalid task number.")