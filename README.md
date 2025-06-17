# 📝 Automated Data Entry Bot for Notepad

A simple Python automation bot that opens Notepad, fetches blog posts from an online API, types them into Notepad like a human, and saves each post as a `.txt` file. The automation uses `PyAutoGUI` for desktop control, `BotCity` for visual recognition and reliability and `requests` to fetch data.

---

## 📌 Features

- Automates launching Notepad.
- Types blog posts with titles and bodies from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/guide/).
- Saves each post in a structured format as `.txt` files.
- Cleans up old `.txt` files before each run.
- Includes basic error handling for reliability.
- Captures screenshots for debugging when errors occur.

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6 or higher
- Notepad must be installed (default on Windows)
- Internet connection to fetch data from API

### 1. Clone the Repository

```bash
git clone https://github.com/MagedWadi/Automated-Data-Entry-Bot-for-Desktop-Application.git
cd Automated-Data-Entry-Bot-for-Desktop-Application
```

### 2. Set Up the Virtual Environment (Windows) (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

⚠️ PowerShell Users: If you get a script execution error, run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```bash
pip install pyautogui requests
pip install botcity-framework-core
```

▶️ Running the Bot

```bash
python automation_bot.py
```

The script will:

1. Clean up .txt files in ~/Desktop/tjm-project.

2. Fetch the first 10 blog posts from JSONPlaceholder.

3. Open Notepad and type each post.

4. Save each post as post X.txt.

5. Handle and log any errors by capturing screenshots.

🧠 How It Works

- Notepad Automation: Launched using subprocess and typed into using PyAutoGUI.write().

- Data Source: Uses the JSONPlaceholder /posts endpoint.

- Save Operation: Automates Ctrl+S and types full save path.

- Cleanup: Deletes existing .txt files before each run.

⚠️Error Handling:

- Failed API requests

- Notepad not opening

- Save errors

- Gracefully skips and logs errors per post

## 📸 Screenshots

Screenshots of failed actions are saved in the `assets/` folder for debugging. For example:  
- `error_launching_Notepad.png`  
- `notepad_not_found_post.png`  
- `error_typing_1.png`

## 📬 Contact

**Author:** Maged Wadi  
📧 **Email:** [maged.wadi14@gmail.com](mailto:maged.wadi14@gmail.com)
