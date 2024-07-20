# Davaleba 27:
import json
import threading

def parse_and_print_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print(f"Data from {filename}: {data}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")

def main():
    filenames = ["file1.json", "file2.json", "file3.json"]
    threads = []

    for filename in filenames:
        thread = threading.Thread(target=parse_and_print_json, args=(filename,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()