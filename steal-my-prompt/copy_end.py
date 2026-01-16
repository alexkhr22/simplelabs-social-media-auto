import os
import shutil

ROOT_DIR = "."
END_FILENAME = "end.png"   # ← falls andere Endung, hier ändern

def copy_end_file():
    source_path = os.path.join(ROOT_DIR, END_FILENAME)

    if not os.path.isfile(source_path):
        print(f"❌ Datei nicht gefunden: {source_path}")
        return

    for root, dirs, _ in os.walk(ROOT_DIR):
        for d in dirs:
            target_dir = os.path.join(root, d)
            target_path = os.path.join(target_dir, END_FILENAME)

            if os.path.exists(target_path):
                print(f"⏭️  Skip (exists): {target_path}")
                continue

            shutil.copy2(source_path, target_path)
            print(f"✅ Kopiert nach: {target_path}")

    print("\n🎉 Fertig! Datei wurde in alle Unterordner kopiert.")

if __name__ == "__main__":
    copy_end_file()
