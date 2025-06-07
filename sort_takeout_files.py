import os
import shutil
import hashlib

base_dir = "/Users/adiiiii/Downloads"
takeout_dirs = takeout_dirs = ["Takeout", "Takeout 2", "Takeout 3", "Takeout 4", "Takeout 5", "Takeout 6"]
source_dirs = [os.path.join(base_dir, d) for d in takeout_dirs]
output_dir = os.path.join(base_dir, "sorted_takeouts")

# File categories
file_categories = {
    "documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".txt", ".xls", ".xlsx"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".heic", ".bmp"],
    "json_files": [".json"],
    "duplicates": [],
    "broken_videos": [],
    "others": []
}

# Make destination folders
dest_paths = {k: os.path.join(output_dir, k) for k in file_categories}
for path in dest_paths.values():
    os.makedirs(path, exist_ok=True)

# Helpers
def classify(file):
    ext = os.path.splitext(file)[1].lower()
    for category, ext_list in file_categories.items():
        if ext in ext_list:
            return category
    return "others"

def is_broken_video(path):
    return os.path.splitext(path)[1].lower() in file_categories["videos"] and os.path.getsize(path) < 100 * 1024

def get_file_hash(path):
    try:
        with open(path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return None

# Scan and move files
seen_hashes = set()
for src_dir in source_dirs:
    for root, _, files in os.walk(src_dir):
        for file in files:
            src = os.path.join(root, file)
            file_hash = get_file_hash(src)

            if file_hash in seen_hashes:
                category = "duplicates"
            else:
                seen_hashes.add(file_hash)
                if is_broken_video(src):
                    category = "broken_videos"
                else:
                    category = classify(file)

            dest_folder = dest_paths[category]
            dest_path = os.path.join(dest_folder, file)

            # Rename if needed to avoid collisions
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(src, dest_path)
            print(f"Moved {file} → {category}/")

print("✅ All Takeout folders sorted into:", output_dir)
