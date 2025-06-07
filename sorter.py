import os
import shutil
import hashlib
from pathlib import Path
from collections import defaultdict

# Define file type categories
DOC_TYPES = {'.doc', '.docx', '.ppt', '.pptx', '.pdf'}
VIDEO_TYPES = {'.mp4', '.mov', '.avi', '.mkv'}
JSON_TYPES = {'.json'}

# Create target folders
base_output = Path("sorted_output")
categories = ['documents', 'videos', 'json', 'duplicates', 'others']
for category in categories:
    (base_output / category).mkdir(parents=True, exist_ok=True)

# Dictionary to track duplicate files by hash
hashes = defaultdict(list)

def file_hash(filepath):
    """Generate a hash for a file's content."""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
    except Exception:
        return None
    return hasher.hexdigest()

def categorize_file(file_path):
    ext = file_path.suffix.lower()
    file_dest = None

    # Duplicate check
    file_md5 = file_hash(file_path)
    if file_md5:
        if file_md5 in hashes:
            file_dest = base_output / 'duplicates'
        else:
            hashes[file_md5].append(str(file_path))

    # Categorization
    if ext in DOC_TYPES:
        file_dest = base_output / 'documents'
    elif ext in VIDEO_TYPES:
        file_dest = base_output / 'videos'
    elif ext in JSON_TYPES:
        file_dest = base_output / 'json'
    elif not file_dest:
        file_dest = base_output / 'others'

    try:
        shutil.copy(file_path, file_dest / file_path.name)
    except Exception as e:
        print(f"Failed to copy {file_path}: {e}")

# Entry folder (change this to your actual folder)
source_folder = Path("takeout_folder")

# Recursively process files
for dirpath, _, filenames in os.walk(source_folder):
    for filename in filenames:
        file_path = Path(dirpath) / filename
        if file_path.is_file():
            categorize_file(file_path)
