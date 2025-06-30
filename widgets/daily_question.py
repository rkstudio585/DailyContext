import os
import random
from datetime import datetime
from widgets.base_widget import Widget

class DailyQuestionWidget(Widget):
    def display(self):
        questions = self.config.get('daily_question', {}).get('questions', [])
        log_file = self.config.get('daily_question', {}).get('log_file')

        if questions:
            question = random.choice(questions)
            print(f"Daily Question: {question}")
            answer = input("Your answer: ")
            if log_file:
                with open(log_file, 'a') as f:
                    f.write(f"\n## {datetime.now().strftime('%Y-%m-%d')}\n")
                    f.write(f"**Question:** {question}\n")
                    f.write(f"**Answer:** {answer}\n")
                print("Answer logged.")
            else:
                print("Warning: Daily log file not configured.")
        else:
            print("Daily Question: No questions configured.")
