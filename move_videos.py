import os
import shutil

# Source folder (where videos are currently stored)
source_dir = "/Users/adiiiii/Downloads/sortedhilmil/keep"

# Destination folder
target_dir = "/Users/adiiiii/Downloads/sortedhilmil/sorted_videos"
os.makedirs(target_dir, exist_ok=True)

# Move all .MOV files
for filename in os.listdir(source_dir):
    if filename.lower().endswith('.mov'):
        src = os.path.join(source_dir, filename)
        dst = os.path.join(target_dir, filename)
        shutil.move(src, dst)
        print(f"✅ Moved: {filename}")

print("🎥 Done! All .MOV files moved.")
# Folder to scan for videos
source_dir = "/Users/adiiiii/Downloads/sortedhilmil/keep"

# Folder to move videos into
target_dir = "/Users/adiiiii/Downloads/sortedhilmil/sorted_videos"
os.makedirs(target_dir, exist_ok=True)

# Move all .MOV and .MP4 files
video_extensions = ('.mov', '.mp4')

for filename in os.listdir(source_dir):
    if filename.lower().endswith(video_extensions):
        src = os.path.join(source_dir, filename)
        dst = os.path.join(target_dir, filename)
        shutil.move(src, dst)
        print(f"🎥 Moved: {filename}")

print("✅ Done! All .MOV and .MP4 files moved.")
