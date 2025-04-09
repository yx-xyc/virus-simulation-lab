import os
import base64
import re

VIRUS_START = "# === VIRUS START ==="
VIRUS_END = "# === VIRUS END ==="

def clean_file(file):
    with open(file, "r") as f:
        lines = f.readlines()

    if VIRUS_START not in ''.join(lines):
        return False

    cleaned_lines = []
    in_virus = False
    for line in lines:
        if VIRUS_START in line:
            in_virus = True
        elif VIRUS_END in line:
            in_virus = False
            continue
        elif not in_virus:
            cleaned_lines.append(line)

    code_str = ''.join(cleaned_lines)

    match = re.search(r"base64\.b64decode\('([^']+)'\)", code_str)
    if match:
        encoded = match.group(1)
        try:
            decoded = base64.b64decode(encoded + "===")
            with open(file, "w") as f:
                f.write(decoded.decode())
        except Exception as e:
            print(f"❌ Failed to decode {file}: {e}")
    else:
        with open(file, "w") as f:
            f.writelines(cleaned_lines)

    return True

def clean_all():
    for file in os.listdir():
        if (file.endswith(".py") and not file.startswith("virus") ):
            if clean_file(file):
                print(f"✅ Cleaned: {file}")

if __name__ == "__main__":
    clean_all()
