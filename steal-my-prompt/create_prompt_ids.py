import os
import re

base_dir = os.getcwd()
pattern = re.compile(r"\((\d+)\)")

for entry in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, entry)

    # nur Ordner
    if not os.path.isdir(folder_path):
        continue

    # ID aus Ordnernamen ziehen
    match = pattern.search(entry)
    if not match:
        continue

    prompt_id = match.group(1)
    file_path = os.path.join(folder_path, "prompt-id.txt")

    # wenn Datei existiert → überspringen
    if os.path.exists(file_path):
        print(f"✔ bereits vorhanden: {entry}")
        continue

    # sonst anlegen
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prompt_id)

    print(f"➕ angelegt: {entry} → ID {prompt_id}")
