## 🗂️ Project Name
**DailyContext**

## 📝 Purpose
Create a **pure Python** terminal application that displays a personalized daily dashboard combining contextual information such as:
- Local date and time
- Random motivational quote
- To-do list from a local `todo.txt` or `todo.md`
- A “Today I Learned” (TIL) note from a local notes folder
- A daily question prompt and store the user’s answer for journaling

## ✅ Requirements
- **Language:** 
    - Python 3 only
- **Cross-platform:** 
    - Should run in Termux or any standard Linux/Mac/Windows terminal
- **Configurable:** 
    - All paths and APIs must be editable in a `config.json` file
- **Modular:** 
    - Each “widget” (quote, prompt, e.g..) must be its own Python class/module
- **Local storage:** 
    - Store daily answers and logs in local files (`daily_log.md`, JSON, or similar)
- **Automation:** 
    - Can be run manually or scheduled with `cron`/`task scheduler`

## 🧩 Features Breakdown
### 1 Date & Time Widget
- Display local date & time in a nice format

### 2 Quote Widget
- Fetch a random motivational quote (API or local quotes file)

### 3 To-Do Widget
- Read tasks from `todo.txt` or `todo.md`
- Show pending tasks

### 4 TIL Widget
- Pick a random note from a `til/` folder and display it

### 5 Daily Question Widget
- Show a daily prompt question (from a list)
- Capture user’s answer and append it to a local log


## 🗂️ File Structure (Example)

- / 
    ├── config.json 
    ├── main.py 
    ├── widgets/ 
    │   ├── init.py 
    │   ├── date_time.py 
    │   ├── quote.py 
    │   ├── todo.py 
    │   ├── til.py 
    │   ├── daily_question.py 
    │   └── reflection.py 
    ├── data/ 
    │   ├── todo.txt 
    │   ├── til/ 
    │   ├── daily_log.md 
    │   └── quotes.txt 
    ├── requirements.txt 
    └── README.md

## 📌 Package Management
- For Python dependencies:
    - use `uv` (`uv pip install <packages_name> --system`)

## 🚀 Execution
- Run manually: `python3 main.py`
- Automate: add to `cron` to run every morning

## ⚙️ Deliverables
- Full working Python code with clear modules
- Well-commented and documented
- DailyContext Config file `config.json`.
- DailyContext explaining for this project `README.md` explaining setup, usage & customization.

## GitHub & Cli
    - Always make a new branch and push on GitHub.
    ```
    git init
    git add .
    git commit -m "<commit-name>"
    git branch -M main
    git remote add origin https://github.com/rkstudio585/DailyContext.git
    git push -u origin main
    ```
