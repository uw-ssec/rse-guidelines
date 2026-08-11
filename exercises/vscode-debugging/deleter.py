import os
from pathlib import Path
from time import sleep


def main():
    print(f"PID: {os.getpid()}")
    file = Path("today.json")
    while True:
        if file.exists():
            print(f"Found {file}, deleting...")
            file.unlink()
            # sys.exit(0)
        sleep(1)
        print(".", end="", flush=True)


if __name__ == "__main__":
    import debugpy

    debugpy.listen(5678)
    main()
