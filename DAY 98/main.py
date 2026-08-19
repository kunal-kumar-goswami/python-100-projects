"""
File Organizer Script
This script organizes files in a specified folder into subfolders based on file type.

Setup for email (optional):
    Set these environment variables before running with --email:
        export MY_EMAIL="you@gmail.com"
        export MY_EMAIL_APP_PASSWORD="your-16-char-gmail-app-password"
        export REPORT_TO_EMAIL="you@gmail.com"   # who receives the report
"""

import argparse
import logging
import os
import shutil
import smtplib
from datetime import datetime
from pathlib import Path


CATEGORY_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt",
                  ".pptx", ".csv", ".md"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Scripts": {".py", ".js", ".html", ".css", ".java", ".cpp", ".sh", ".json"},
}

LOG_FILE = "file_organizer.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def get_category(extension: str) -> str:
    """Return the category folder name for a given file extension."""
    extension = extension.lower()
    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category
    return "Others"


def organize_folder(target_path: str) -> dict:
    """
    Organize all files in target_path into category subfolders.
    Returns a summary dict: {category: [filenames moved]}
    """
    target = Path(target_path).expanduser().resolve()

    if not target.is_dir():
        raise NotADirectoryError(f"'{target}' is not a valid directory.")

    summary = {category: [] for category in list(CATEGORY_MAP.keys()) + ["Others"]}

    files = [f for f in target.iterdir() if f.is_file()]
    logger.info(f"Found {len(files)} file(s) in {target}")

    for file_path in files:
        category = get_category(file_path.suffix)
        dest_folder = target / category
        dest_folder.mkdir(exist_ok=True)

        dest_path = dest_folder / file_path.name

        # Avoid overwriting files with the same name
        if dest_path.exists():
            stem, suffix = file_path.stem, file_path.suffix
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            dest_path = dest_folder / f"{stem}_{timestamp}{suffix}"

        shutil.move(str(file_path), str(dest_path))
        summary[category].append(file_path.name)
        logger.info(f"Moved '{file_path.name}' -> {category}/")

    return summary


def build_report(summary: dict, target_path: str) -> str:
    """Turn the summary dict into a readable text report."""
    total = sum(len(v) for v in summary.values())
    lines = [
        "FILE ORGANIZER REPORT",
        f"Folder: {target_path}",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total files organized: {total}",
        "-" * 40,
    ]
    for category, filenames in summary.items():
        if filenames:
            lines.append(f"{category} ({len(filenames)}):")
            for name in filenames:
                lines.append(f"   - {name}")
    if total == 0:
        lines.append("No files needed organizing. Folder was already clean!")
    return "\n".join(lines)


def email_report(report_text: str) -> None:
    """Send the report via Gmail SMTP using env-var credentials."""
    my_email = os.environ.get("MY_EMAIL")
    app_password = os.environ.get("MY_EMAIL_APP_PASSWORD")
    to_email = os.environ.get("REPORT_TO_EMAIL", my_email)

    if not my_email or not app_password:
        logger.warning(
            "Email requested but MY_EMAIL / MY_EMAIL_APP_PASSWORD env vars "
            "are not set. Skipping email step."
        )
        return

    message = (
        f"Subject: Your File Organizer Report - {datetime.now().strftime('%Y-%m-%d')}\n\n"
        f"{report_text}"
    )

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, app_password)
            connection.sendmail(my_email, to_email, message.encode("utf-8"))
        logger.info(f"Report emailed to {to_email}")
    except smtplib.SMTPException as e:
        logger.error(f"Failed to send email report: {e}")



def main():
    parser = argparse.ArgumentParser(
        description="Organize a folder's files into category subfolders."
    )
    parser.add_argument(
        "--path", required=True, help="Path to the folder you want organized."
    )
    parser.add_argument(
        "--email", action="store_true",
        help="Email the summary report (requires MY_EMAIL and "
             "MY_EMAIL_APP_PASSWORD env vars)."
    )
    args = parser.parse_args()

    summary = organize_folder(args.path)
    report = build_report(summary, args.path)

    print("\n" + report + "\n")

    if args.email:
        email_report(report)


if __name__ == "__main__":
    main()