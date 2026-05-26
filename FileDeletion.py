import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Folder path
FOLDER_PATH = r"/home/bandaru/Documents/MyFile/"   # Change this path

# File extension to delete
FILE_EXTENSION = ".txt"


def delete_files(folder_path, extension):
    """
    Delete files with a specific extension from a folder.
    """

    path = Path(folder_path)

    # Check if folder exists
    if not path.exists():
        logging.error(f"Folder does not exist: {folder_path}")
        return

    # Get matching files
    files = path.glob(f"*{extension}")

    deleted_count = 0

    for file in files:
        try:
            if file.is_file():
                file.unlink()
                logging.info(f"Deleted: {file}")
                deleted_count += 1

        except Exception as e:
            logging.error(f"Failed to delete {file}: {e}")

    logging.info(f"Total deleted files: {deleted_count}")


if __name__ == "__main__":
    delete_files(FOLDER_PATH, FILE_EXTENSION)