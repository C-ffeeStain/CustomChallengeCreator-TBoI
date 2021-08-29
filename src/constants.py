from pathlib import Path
import sys

IS_EXE = False

BASE_DIR: Path = Path(__file__).resolve().parent

if hasattr(sys, "_MEIPASS"):
    print(sys._MEIPASS)
    BASE_DIR = BASE_DIR / getattr(sys, "_MEIPASS")
    IS_EXE = True
