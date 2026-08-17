from pathlib import Path

# 1. Custom Logger Class representing OOPs integration with File Handling
class Logger:
    """
    A simple file logger class demonstrating append operations.
    """
    def __init__(self, file_path: str):
        self.path = Path(file_path)
        
        # Touch the file to ensure it exists
        try:
            with open(self.path, "a", encoding="utf-8"):
                pass
        except PermissionError:
            print(f"Permission Error: Cannot initialize log file at '{self.path}'")

    def log(self, message: str):
        try:
            # Context manager (with) automatically closes the stream
            with open(self.path, "a", encoding="utf-8") as writer:
                writer.write(message + "\n")
        except Exception as e:
            print(f"Failed to log message: '{message}'. Error: {e}")


def main():
    sample_file = "example.txt"
    log_file = "application.log"

    print("--- 1. Creating and Writing to a File ---")
    try:
        # 'w' mode overwrites the file, or creates it if missing
        with open(sample_file, "w", encoding="utf-8") as writer:
            writer.write("Hello, world!\n")
            writer.write("This is a sample file for file handling demonstration.\n")
        print(f"File '{sample_file}' created and written successfully.")
    except Exception as e:
        print(f"Failed to create/write file. Error: {e}")
    print()

    print("--- 2. Checking File Properties ---")
    p = Path(sample_file)
    if p.exists():
        print(f"File Name:     {p.name}")
        print(f"Absolute Path: {p.resolve()}")
        print(f"File Size:     {p.stat().st_size} bytes")
    else:
        print(f"File '{sample_file}' does not exist.")
    print()

    print("--- 3. Reading a File Line-by-Line ---")
    try:
        # 'r' mode reads. Iterating line-by-line is memory efficient.
        with open(sample_file, "r", encoding="utf-8") as reader:
            for index, line in enumerate(reader, 1):
                # strip() cleans up trailing newline characters
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"Failed to read file. Error: {e}")
    print()

    print("--- 4. Logging Application Data ---")
    my_logger = Logger(log_file)
    my_logger.log("Info: Application started...")
    my_logger.log("Warning: Database response delayed.")
    my_logger.log("Error: Connection timeout.")
    
    # Read back log results
    print("Reading log results:")
    with open(log_file, "r", encoding="utf-8") as log_reader:
        for line in log_reader:
            print(f"  [LOG] {line.strip()}")
    print()

    print("--- 5. Cleaning Up Temp Files ---")
    try:
        # Delete files using pathlib
        Path(sample_file).unlink()
        Path(log_file).unlink()
        print("Successfully cleaned up example.txt and application.log.")
    except Exception as e:
        print(f"Failed to clean up files. Error: {e}")


if __name__ == "__main__":
    main()
