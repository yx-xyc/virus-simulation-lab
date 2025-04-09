# 🧬 Virus Simulation Lab (For Educational Use Only)

This project is a **safe, controlled simulation** of how a basic computer virus might propagate and be detected or removed. It is **strictly for learning, ethical hacking, and cybersecurity education**.

> ⚠️ No real malware or destructive code is used. The simulation is safe, non-destructive, and operates only on local `.py` files.

---

## 🔧 Features

- Simulated virus that:
  - Infects local `.py` files (excluding those starting with `virus`)
  - Injects its payload and base64-encodes the original content
  - Logs infection activity with timestamps
- Cleaner to restore infected files
- Lab Manager CLI to control the simulation
- Modular virus structure with the payload in a separate file

---

## 🚀 How to Run

### 1. Create a virtual environment (recommended)

```bash
cd sim_virus_project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Start the lab manager CLI

```bash
python virus_manager.py
```

Follow the on-screen menu to:

- Simulate virus infections
- Clean infected files
- View the infection log
- Check infection status of all `.py` files
- Exit virus manager

---

## 🧹 Cleaning Infected Files

You can clean infected files at any time with:

```bash
python virus_cleaner.py
```

This will restore infected files to their original state.

---

## 📝 Logging

Infected files are recorded in `virus_log.txt` in the format:

```
Infected: 2025-04-08 22:53:37 | target2.py
```

Each line logs a timestamp and the name of a newly infected file.

---

## ✅ Safety Rules

- Files starting with `virus` (e.g. `virus_sim.py`, `virus_body.py`) will **not be infected**.
- The simulation only modifies local `.py` files in the current directory.
- Infections are reversible via `cleaner.py`.

---

## ⚠️ Disclaimer

This project is for **educational and ethical use only**. Do not use any code from this project to harm others or compromise real-world systems. Always test in a controlled, sandboxed environment such as:

- A Python virtual environment
- A Docker container
- A virtual machine

---

## 📚 Inspired By

- Intro to malware behavior simulation
- Self-replicating code (quine-style)
- Python scripting in cybersecurity education

---

## 📌 License

This project is open-source and provided as-is, with no guarantees. Use responsibly.
