import os
import random
from rich.panel import Panel
from rich.text import Text

class TILWidget:
    def __init__(self, config):
        self.config = config

    def get_content(self):
        til_folder = self.config['paths']['til_folder']
        try:
            notes = [f for f in os.listdir(til_folder) if os.path.isfile(os.path.join(til_folder, f))]
            if not notes or (len(notes) == 1 and notes[0] == 'placeholder.txt'):
                return Panel(Text("No TIL notes found.", justify="center"), title="Today I Learned", border_style="yellow")

            random_note_file = random.choice([note for note in notes if note != 'placeholder.txt'])
            with open(os.path.join(til_folder, random_note_file), 'r') as f:
                content = f.read()
            
            text = Text(content)
            return Panel(text, title=f"TIL: {random_note_file}", border_style="yellow")
        except FileNotFoundError:
            return Panel(Text("til/ folder not found.", justify="center"), title="Today I Learned", border_style="red")
