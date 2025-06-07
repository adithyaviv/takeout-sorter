# Takeout Sorter

A Python script developed using AI-assisted "vibe coding" to recursively organize Google Takeout exports.

### Features
- Recursively scans nested folders
- Sorts files into:
  - Documents (.doc, .pdf, .ppt)
  - Videos (.mp4, .mov, etc.)
  - JSON metadata
  - Duplicate files (using MD5 hash comparison)
  - Uncategorized (others)
- Output is stored in a clean folder structure

### Usage
1. Place your exported Google Takeout files in a folder called `takeout_folder` (same level as the script).
2. Run the script:  
   ```bash
   python sorter.py
