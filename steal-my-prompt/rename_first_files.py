import os

ROOT_DIR = "."
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

def rename_first_images():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            lower_name = file.lower()

            if "first" not in lower_name:
                continue

            if not lower_name.endswith(SUPPORTED_FORMATS):
                continue

            old_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            new_name = f"first{ext}"
            new_path = os.path.join(root, new_name)

            if os.path.exists(new_path):
                print(f"⏭️  Skip (exists): {new_path}")
                continue

            os.rename(old_path, new_path)
            print(f"✅ Renamed: {old_path} → {new_path}")

    print("\n🎉 Fertig! Alle passenden Bilder wurden umbenannt.")

if __name__ == "__main__":
    rename_first_images()
