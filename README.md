# DailyContext

A pure Python terminal application that displays a personalized daily dashboard.

## ✨ Features

- **Date & Time:** Shows the current date and time.
- **Quote of the Day:** Fetches a random motivational quote.
- **To-Do List:** Displays your pending tasks from a local file.
- **Today I Learned (TIL):** Shows a random note from your collection.
- **Daily Question:** Prompts you with a daily question for journaling.

## 🚀 Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rkstudio585/DailyContext.git
    cd DailyContext
    ```

2.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt --system
    ```

## Usage

To run the application:

```bash
python3 main.py
```

## ⚙️ Configuration

All settings are in the `config.json` file:

- `paths`: Set the paths to your local files for to-do lists, TIL notes, etc.
- `quote_api_url`: The API endpoint for fetching quotes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
