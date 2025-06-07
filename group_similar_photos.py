import os
import shutil
from PIL import Image
import imagehash

# Source folder with images to group
source_dir = "/Users/adiiiii/Downloads/sortedhilmil/keep"
target_dir = "/Users/adiiiii/Downloads/sortedhilmil/similar_groups"
os.makedirs(target_dir, exist_ok=True)

# Threshold for visual similarity (0 = exact match, 5 = visually similar)
similarity_threshold = 5

# Get all image files
all_images = [f for f in os.listdir(source_dir)
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Track processed images and their hashes
hashes = {}

# Loop more efficiently: only compare new images to earlier ones
for i, filename in enumerate(all_images):
    img_path = os.path.join(source_dir, filename)
    if not os.path.exists(img_path):  # May have been moved already
        continue

    try:
        img = Image.open(img_path)
        img_hash = imagehash.phash(img)
        img.close()
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        continue

    # Compare only to previously hashed images
    found_similar = None
    for ref_name, ref_hash in hashes.items():
        if img_hash - ref_hash <= similarity_threshold:
            found_similar = ref_name
            break

    if found_similar:
        # Move both files to group folder
        group_folder = os.path.join(target_dir, f"similar_to_{found_similar}")
        os.makedirs(group_folder, exist_ok=True)

        ref_path = os.path.join(source_dir, found_similar)
        if os.path.exists(ref_path):
            shutil.move(ref_path, os.path.join(group_folder, found_similar))
        shutil.move(img_path, os.path.join(group_folder, filename))
    else:
        hashes[filename] = img_hash  # Save hash only if not moved

print("✅ Done! Similar images moved to 'similar_groups'")
