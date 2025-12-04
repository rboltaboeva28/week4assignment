def sanitize_filenames(files):
    filename = []
    for n in files:
        name = n.strip().lower().replace(" ", "_")
        if "txt" in name:
            filename.append(name)
    return filename

uploads = [
    "  My Resume.pdf ",  # Not a .txt file, skip
    "Vacation Photo.JPG", # Not a .txt file, skip
    "PROJECT specs.txt",
    "   ",
    "notes.txt"
]

# Run the function
safe_files = sanitize_filenames(uploads)
print(safe_files)