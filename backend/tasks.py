# app / tasks.py
import os
import sys
import subprocess

def run():
    subprocess.run(["uvicorn", "backend.app.main:app", "--reload"])

def test():
    os.environ["ENVIRONMENT"] = "testing"
    subprocess.run(["pytest", "backend/tests/"])  # Explicitly specify the tests directory


def initdb():
    subprocess.run(["python", "-m", "app.database.init"])

def migrate():
    subprocess.run(["alembic", "revision", "--autogenerate", "-m", "Your migration message here"])

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else None
    if task == "run":
        run()
    elif task == "test":
        test()
    elif task == "initdb":
        initdb()
    elif task == "migrate":
        migrate()
    else:
        print("Invalid task.")
