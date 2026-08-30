<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2098/day98banner.png" alt="Day 98 - File Organizer Banner" width="100%">
</p>

# Day 98 - Professional Portfolio: Python Automation — File Organizer 🗂️🤖

A genuinely useful command-line automation tool: scans a target folder, sorts every file into category subfolders based on its extension (Images, Documents, Videos, Audio, Archives, Scripts, Others), logs every action, and can optionally email a summary report.

## 🗂️ Project Structure

```
DAY 98/
├── main.py
├── file_organizer.log      # created automatically at runtime
└── README.md
```

## ⚙️ How It Works

- **`CATEGORY_MAP`:** a dictionary mapping category names to sets of file extensions, making it easy to add new categories or extensions later.
- **`get_category(extension)`:** looks up which category a given extension belongs to, defaulting to `"Others"` for anything unrecognized.
- **`organize_folder(target_path)`:** the core logic — resolves the target path, validates it's a real directory, iterates over every file (not subfolders) in it, determines its category, creates the destination subfolder if needed, and moves the file there. If a file with the same name already exists at the destination, it appends a timestamp to avoid overwriting. Returns a summary dict of what was moved where.
- **`build_report(summary, target_path)`:** turns the summary into a clean, readable text report — folder path, timestamp, total files organized, and a breakdown by category.
- **`email_report(report_text)`:** optionally emails the report via Gmail SMTP, reading credentials from environment variables (`MY_EMAIL`, `MY_EMAIL_APP_PASSWORD`, `REPORT_TO_EMAIL`) rather than hardcoding them — and gracefully skips the email step with a warning if those variables aren't set, rather than crashing.
- **Logging:** uses Python's built-in `logging` module, writing timestamped INFO-level logs to both a log file (`file_organizer.log`) and the console — a proper production-style logging setup rather than scattered `print()` statements.
- **CLI interface:** uses `argparse` for a real command-line tool experience — `--path` (required) specifies the folder to organize, and `--email` (optional flag) triggers the email report step.

## 🧠 Concepts Practiced

- Building a genuinely reusable CLI tool with `argparse`
- File system operations with `pathlib` and `shutil` (safer, more modern alternatives to raw `os` path manipulation)
- Proper logging setup (`logging.basicConfig` with both file and console handlers) instead of print debugging
- Environment-variable-based credential management, with a graceful fallback when they're missing
- Handling filename collisions safely (timestamp-based renaming instead of overwriting)
- Structuring a script with clear separation of concerns: categorization, file operations, reporting, and notification as distinct functions
- Optional/flag-based CLI behavior (`--email` as an `action="store_true"` flag)

## 🚀 Run It

```bash
pip install argparse  # (built into Python 3, no install needed)

# Basic usage
python main.py --path "/path/to/messy/folder"

# With an emailed report
export MY_EMAIL="you@gmail.com"
export MY_EMAIL_APP_PASSWORD="your-16-char-gmail-app-password"
export REPORT_TO_EMAIL="you@gmail.com"
python main.py --path "/path/to/messy/folder" --email
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
