import sys
import os
from datetime import datetime


def extract_logs_for_date(log_file_path, target_date):


    try:
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
        target_date_str = target_date_obj.strftime("%Y-%m-%d")  # Normalize format
    except ValueError:
        print(f"Error: Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)


    parent_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(os.path.dirname(parent_dir), "output")
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f"output_{target_date}.txt")


    try:
        print(f"Looking for log file at: {log_file_path}")  # Debug statement
        with open(log_file_path, 'r', encoding='utf-8') as log_file, \
                open(output_file_path, 'w', encoding='utf-8') as output_file:

            # Process the log file line-by-line
            for line in log_file:
                # Check if the line starts with the target date
                if line.startswith(target_date_str):
                    output_file.write(line)
                elif line[:10] > target_date_str:
                    # Stop processing if we've passed the target date
                    break

    except FileNotFoundError:
        print(f"Error: Log file not found at {log_file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

    print(f"Logs for {target_date} have been extracted to {output_file_path}")


if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python log_extraction.py YYYY-MM-DD")
        sys.exit(1)


    target_date = sys.argv[1]


    parent_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(os.path.dirname(parent_dir), "logs_2024.log")  # Updated file name


    extract_logs_for_date(log_file_path, target_date)