import os
import shutil
import re
from datetime import datetime

source_dir = r"/Users/adiiiii/Downloads/thething"
target_dir = r"/Users/adiiiii/Downloads/sorted ones"

os.makedirs(target_dir, exist_ok=True)

# Regular expression to match date in filename like "2025-04-18"
date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')

for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filename)

    if os.path.isfile(filepath):
        match = date_pattern.search(filename)
        if match:
            date_str = match.group(1)  # e.g., "2025-04-18"
            date = datetime.strptime(date_str, "%Y-%m-%d")
            folder_name = f"{date.year}-{date.month:02}"  # e.g., "2025-04"
        else:
            folder_name = "UnknownDate"

        destination = os.path.join(target_dir, folder_name)
        os.makedirs(destination, exist_ok=True)

        shutil.copy(filepath, os.path.join(destination, filename))  # or use shutil.move
