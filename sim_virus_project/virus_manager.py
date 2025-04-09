import os
import subprocess

def run_virus():
    print("🦠 Running virus simulation...")
    subprocess.run(["python", "virus_sim.py"])

def run_cleaner():
    print("🧹 Cleaning infected files...")
    subprocess.run(["python", "virus_cleaner.py"])

def view_log():
    print("📜 Infection log:")
    if os.path.exists("virus_log.txt"):
        with open("virus_log.txt", "r") as f:
            print(f.read())
    else:
        print("No log found.")

def check_status():
    print("🧬 Infection status of .py files:")
    for file in os.listdir():
        if file.endswith(".py") and not file.startswith("virus"):
            with open(file, "r") as f:
                content = f.read()
                status = "🧪 INFECTED" if "# === VIRUS START ===" in content else "✅ CLEAN"
                print(f"{file:<20} {status}")

def menu():
    while True:
        print("\n📦 Virus Simulation Lab")
        print("1. Run virus simulation")
        print("2. Clean infected files")
        print("3. View infection log")
        print("4. Check infection status")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            run_virus()
        elif choice == "2":
            run_cleaner()
        elif choice == "3":
            view_log()
        elif choice == "4":
            check_status()
        elif choice == "5":
            print("👋 Exiting lab manager.")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
