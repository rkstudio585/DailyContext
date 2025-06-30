import os
import random
from widgets.base_widget import Widget

class TilWidget(Widget):
    def display(self):
        folder_path = self.config.get('til', {}).get('folder_path')
        if folder_path and os.path.exists(folder_path):
            til_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if til_files:
                random_til_file = random.choice(til_files)
                with open(os.path.join(folder_path, random_til_file), 'r') as f:
                    content = f.read().strip()
                print(f"Today I Learned ({random_til_file}):\n{content}")
            else:
                print("Today I Learned: No TIL notes found.")
        else:
            print("Today I Learned: TIL folder not found.")
