import os
from widgets.config import Config
from widgets.date_time import DateTimeWidget
from widgets.quote import QuoteWidget
from widgets.todo import TodoWidget
from widgets.til import TilWidget
from widgets.daily_question import DailyQuestionWidget
from widgets.system_info import SystemInfoWidget
from widgets.greeting import GreetingWidget

def display_dashboard(config):
    greeting_widget = GreetingWidget(config)
    greeting_widget.display()

    print("\n--- DailyContext Dashboard ---")

    date_time_widget = DateTimeWidget(config)
    date_time_widget.display()

    quote_widget = QuoteWidget(config)
    quote_widget.display()

    todo_widget = TodoWidget(config)
    todo_widget.display()

    til_widget = TilWidget(config)
    til_widget.display()

    daily_question_widget = DailyQuestionWidget(config)
    daily_question_widget.display()

    system_info_widget = SystemInfoWidget(config)
    system_info_widget.display()

    print("------------------------------\n")

def main():
    config = Config()

    while True:
        print("\nDailyContext Menu:")
        print("1. Display Dashboard")
        print("2. Manage To-Do List")
        print("3. Manage TIL Notes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_dashboard(config)
        elif choice == '2':
            todo_widget_instance = TodoWidget(config)
            while True:
                print("\n--- To-Do List Management ---")
                todo_widget_instance.display()
                print("1. Add Task")
                print("2. Mark Task Complete")
                print("3. Remove Task")
                print("4. Back to Main Menu")
                todo_choice = input("Enter your choice: ")

                if todo_choice == '1':
                    task = input("Enter new task: ")
                    todo_widget_instance.add_task(task)
                elif todo_choice == '2':
                    try:
                        task_num = int(input("Enter task number to mark complete: "))
                        todo_widget_instance.mark_complete(task_num)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif todo_choice == '3':
                    try:
                        task_num = int(input("Enter task number to remove: "))
                        todo_widget_instance.remove_task(task_num)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif todo_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            til_widget_instance = TilWidget(config)
            while True:
                print("\n--- TIL Notes Management ---")
                print("1. Add New TIL")
                print("2. Search TILs")
                print("3. List All TILs")
                print("4. Back to Main Menu")
                til_choice = input("Enter your choice: ")

                if til_choice == '1':
                    title = input("Enter TIL title: ")
                    content = input("Enter TIL content: ")
                    til_widget_instance.add_til(title, content)
                elif til_choice == '2':
                    keyword = input("Enter search keyword: ")
                    found_tils = til_widget_instance.search_til(keyword)
                    if found_tils:
                        print("\nFound TILs:")
                        for filename, content in found_tils:
                            print(f"--- {filename} ---")
                            print(content)
                            print("---------------------")
                    else:
                        print("No TILs found matching your keyword.")
                elif til_choice == '3':
                    all_tils = til_widget_instance.list_tils()
                    if all_tils:
                        print("\nAll TILs:")
                        for til_file in all_tils:
                            print(f"- {til_file}")
                    else:
                        print("No TIL notes found.")
                elif til_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '4':
            print("Exiting DailyContext. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()