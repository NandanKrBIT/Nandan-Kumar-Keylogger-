# Reads log file and prints analysis
def analyze_logs(log_file="key_log.txt"):
    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
            print(f"Total keystrokes recorded: {len(lines)}")
            print("Sample log entries:")
            print("".join(lines[:10]))
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    analyze_logs()
