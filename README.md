# 🛡️ SOC Log Analysis Dashboard

A Python-based SIEM (Security Information and Event Management) dashboard for **Windows and Firewall log analysis**, built for SOC (Security Operations Center) monitoring and threat detection.

---

## Features

- Parse **Windows security logs** and **Firewall logs**.
- Detect security events:
  - Brute-force login attempts
  - Credential stuffing
  - Firewall blocked attacks on sensitive ports (22, 3389)
- Switch between log types with **interactive dashboard**.
- Alert display with **raw logs and detected threats**.
- Built with **Python** and **Streamlit**.

---

## Tech Stack

- **Python 3.11**
- **Streamlit** – interactive dashboard
- **VS Code** – development environment

---

## Setup & Run

1. Clone the repo:

```bash
git clone https://github.com/Urusha-Lama/SOC-Log-Dashboard.git
cd SOC-Log-Dashboard

2.Create virtual environment:
python -m venv .venv
.venv\Scripts\activate  # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run dashboard:
python -m streamlit run dashboard.py

## Project Structure
SOC-Log-Dashboard/
 ├── dashboard.py           # Main Streamlit dashboard
 ├── parse_windows.py       # Windows log parser
 ├── parse_firewall.py      # Firewall log parser
 ├── detection_engine.py    # Threat detection logic
 ├── windows_logs.txt       # Sample Windows logs
 ├── firewall_logs.txt      # Sample Firewall logs
 └── README.md
 └──.gitignore


##Future Improvements

Correlate Windows and Firewall logs in real-time

Visualize alerts with charts and timelines

Integrate MITRE ATT&CK framework for event mapping

Support real .evtx Windows logs


##Author
Urusha Lama – Aspiring SOC Analyst


