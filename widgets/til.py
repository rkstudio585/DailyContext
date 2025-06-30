"""Widget to display a random 'Today I Learned' (TIL) note.

This widget picks a random file from the TIL folder and displays its content.
"""
import os
import random
from rich.panel import Panel
from rich.text import Text

class TILWidget:
    """A widget to display a random TIL note."""
    def __init__(self, config):
        """Initializes the TILWidget with configuration."""
        self.config = config

    def get_content(self):
        """Generates a panel with a random TIL note."""
        til_folder = self.config['paths']['til_folder']
        try:
            notes = [f for f in os.listdir(til_folder) if os.path.isfile(os.path.join(til_folder, f))]
            if not notes or (len(notes) == 1 and notes[0] == 'placeholder.txt'):
                return Panel(Text("No TIL notes found.", justify="center"), title="Today I Learned", border_style="yellow")

            # Exclude placeholder from random choice
            notes = [note for note in notes if note != 'placeholder.txt']
            if not notes:
                 return Panel(Text("No TIL notes found.", justify="center"), title="Today I Learned", border_style="yellow")

            random_note_file = random.choice(notes)
            with open(os.path.join(til_folder, random_note_file), 'r') as f:
                content = f.read()
            
            text = Text(content)
            return Panel(text, title=f"TIL: {random_note_file}", border_style="yellow")
        except FileNotFoundError:
            return Panel(Text("til/ folder not found.", justify="center"), title="Today I Learned", border_style="red")