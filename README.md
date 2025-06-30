# DailyContext

DailyContext is a pure Python terminal application that provides a personalized daily dashboard. It combines contextual information such as the local date and time, a random motivational quote, a to-do list, a "Today I Learned" (TIL) note, and a daily question prompt for journaling.

## Features

- **Date & Time Widget:** Displays the current local date and time.
- **Quote Widget:** Fetches and displays a random motivational quote from a local file.
- **To-Do Widget:** Manages and displays pending tasks from a `todo.txt` file, allowing users to add, remove, and mark tasks as complete.
- **TIL Widget:** Manages and displays "Today I Learned" notes from a `til/` folder, allowing users to add new notes, search existing ones, and list all notes.
- **Daily Question Widget:** Presents a daily prompt question and records the user's answer to a local log file.
- **System Information Widget:** Displays basic system details like operating system, architecture, Python version, disk usage, and uptime.
- **Greeting Widget:** Provides a customizable greeting based on the time of day.

## Interactive Mode

The application now features an interactive menu, allowing users to navigate between different functionalities:

-   **Display Dashboard:** Shows all the widgets in a single view.
-   **Manage To-Do List:** Provides options to interact with your to-do tasks.
-   **Manage TIL Notes:** Provides options to interact with your TIL notes.

## Setup

1.  **Clone the repository (if applicable) or create the project structure:**

    ```bash
    # If you have git installed
    git clone https://github.com/rkstudio585/DailyContext.git
    cd DailyContext
    ```

    If not cloning, ensure you have the following directory structure:

    ```
    DailyContext/
    ├── config.json
    ├── main.py
    ├── widgets/
    │   └── __init__.py
    ├── data/
    │   ├── todo.txt
    │   ├── til/
    │   ├── daily_log.md
    │   └── quotes.txt
    └── requirements.txt
    ```

2.  **Install dependencies:**

    DailyContext is designed to be pure Python and currently has no external dependencies beyond standard Python libraries. If any are added in the future, they will be listed in `requirements.txt`.

    You can use `uv` to manage Python packages:

    ```bash
    uv pip install -r requirements.txt --system
    ```

3.  **Configuration:**

    Edit the `config.json` file to customize paths and settings for each widget:

    ```json
    {
        "date_time": {
            "format": "%Y-%m-%d %H:%M:%S"
        },
        "quote": {
            "source": "local",
            "file_path": "data/quotes.txt"
        },
        "todo": {
            "file_path": "data/todo.txt"
        },
        "til": {
            "folder_path": "data/til"
        },
        "daily_question": {
            "questions": [
                "What is one thing you are grateful for today?",
                "What challenge did you overcome today?",
                "What did you learn today?",
                "What is your intention for tomorrow?"
            ],
            "log_file": "data/daily_log.md"
        }
    }
    ```

    -   `date_time.format`: Python `strftime` format for date and time.
    -   `quote.file_path`: Path to a text file where each line is a motivational quote.
    -   `todo.file_path`: Path to your `todo.txt` or `todo.md` file.
    -   `til.folder_path`: Path to a folder containing your TIL notes (each note as a separate file).
    -   `daily_question.questions`: A list of questions for the daily prompt.
    -   `daily_question.log_file`: Path to the Markdown file where daily answers will be logged.

4.  **Populate Data Files:**

    -   `data/quotes.txt`: Add motivational quotes, one per line.
    -   `data/todo.txt`: Add your to-do tasks, one per line.
    -   `data/til/`: Create text files inside this folder for your TIL notes. Each file can contain one TIL entry.

## Usage

To run the DailyContext application, simply execute the `main.py` script:

```bash
python3 main.py
```

The application will display the dashboard and then prompt you for your answer to the daily question.

## Automation

You can automate the execution of DailyContext using `cron` (on Linux/macOS) or Task Scheduler (on Windows) to run it daily, for example, every morning.

**Example `cron` entry (runs every day at 8:00 AM):**

```cron
0 8 * * * /usr/bin/python3 /path/to/your/DailyContext/main.py
```

Make sure to replace `/usr/bin/python3` with the actual path to your Python 3 executable and `/path/to/your/DailyContext/main.py` with the absolute path to your `main.py` file.

## Customization

-   **Widgets:** Each widget is implemented as a separate class in `main.py` (or can be moved to `widgets/` for larger projects). You can easily create new widgets by inheriting from the `Widget` class and implementing the `display` method.
-   **Configuration:** All paths and settings are managed through `config.json`, allowing for easy customization without modifying the code.
-   **Styling:** For more advanced terminal styling, you could integrate libraries like `rich` (though it's not a dependency by default to keep it pure Python).
