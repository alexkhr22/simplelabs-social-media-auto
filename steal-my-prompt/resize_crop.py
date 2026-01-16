import os
import tempfile
from PIL import Image, ImageOps

ROOT_DIR = "."
TARGET_SIZE = (1080, 1350)
QUALITY = 95

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

def safe_save(img, path):
    ext = os.path.splitext(path)[1].lower()
    dir_name = os.path.dirname(path)
    
    # Temporäre Datei erstellen
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, suffix=ext)
    try:
        # Den Dateideskriptor 'fd' schließen, damit Pillow in den Pfad schreiben kann
        os.close(fd)
        
        if ext in (".jpg", ".jpeg"):
            img.save(tmp_path, quality=QUALITY, optimize=True)
        else:
            img.save(tmp_path)

        # Sicherstellen, dass das Originalbild wirklich zu ist (im Hauptloop wichtig)
        os.replace(tmp_path, path)
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise e


def process_image(path):
    # 'with' stellt sicher, dass die Datei nach dem Block geschlossen wird
    with Image.open(path) as img:
        img = ImageOps.exif_transpose(img)
        if img.size == TARGET_SIZE:
            print(f"⏭️  Skip: {path}")
            return
        
        img = img.convert("RGB")
        img = ImageOps.fit(img, TARGET_SIZE, method=Image.LANCZOS)
        
        # Kopie im RAM erstellen
        final_img = img.copy()

    # Hier ist 'img' (die Originaldatei) bereits geschlossen
    safe_save(final_img, path)
    final_img.close()

def main():
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):
                process_image(os.path.join(root, file))

    print("\n🎉 Alle Bilder fehlerfrei verarbeitet.")


if __name__ == "__main__":
    main()
