import os
import subprocess

# 💡 Path to Ghidra Headless Analyzer
GHIDRA_HEADLESS = r"C:\Users\psypa\Desktop\ghidra_11.3.2_PUBLIC\support\analyzeHeadless.bat"

# 💼 Ghidra project setup
PROJECT_DIR = r"C:\Users\psypa\Desktop\test1\ghidra_project"  # Ensure this folder exists or gets created
PROJECT_NAME = "auto_proj"

# 📦 Binary input
INPUT_BINARY = r"C:\Users\psypa\Desktop\BintoAssembled\lmao.exe"

# 📜 Custom Jython script to use
SCRIPT_PATH = r"C:\Users\psypa\Desktop\BintoAssembled\export_c.py"

# 📂 Output directory (not used directly by Ghidra, but your script writes here)
OUTPUT_DIR = r"C:\Users\psypa\Desktop\BintoAssembled"
os.makedirs(PROJECT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ⚙️ Run Headless Analyzer with your custom script
subprocess.run([
    GHIDRA_HEADLESS,
    PROJECT_DIR,
    PROJECT_NAME,
    "-import", INPUT_BINARY,
    "-scriptPath", os.path.dirname(SCRIPT_PATH),
    "-postScript", os.path.basename(SCRIPT_PATH),
    "-overwrite",
    "-deleteProject"  # Optional: delete after export
])
