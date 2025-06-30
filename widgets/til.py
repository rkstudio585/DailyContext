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

    def _get_til_files(self):
        folder_path = self.config.get('til', {}).get('folder_path')
        if folder_path and os.path.exists(folder_path):
            return sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
        return []

    def add_til(self, title, content):
        folder_path = self.config.get('til', {}).get('folder_path')
        if not folder_path:
            print("TIL folder not configured.")
            return
        os.makedirs(folder_path, exist_ok=True)
        file_name = f"{title.replace(' ', '_').lower()}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"TIL '{title}' added.")

    def search_til(self, keyword):
        folder_path = self.config.get('til', {}).get('folder_path')
        if not folder_path or not os.path.exists(folder_path):
            print("TIL folder not found.")
            return []

        found_tils = []
        for filename in self._get_til_files():
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                content = f.read()
                if keyword.lower() in content.lower() or keyword.lower() in filename.lower():
                    found_tils.append((filename, content))
        return found_tils

    def list_tils(self):
        folder_path = self.config.get('til', {}).get('folder_path')
        if not folder_path or not os.path.exists(folder_path):
            print("TIL folder not found.")
            return []
        return self._get_til_files()