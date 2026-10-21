# Python Port Scanner 🔐

A lightweight TCP port scanner built with Python to explore network scanning, socket programming, and fundamental cybersecurity concepts.

## 📌 Overview

This tool accepts an IP address or hostname, resolves the target to an IPv4 address, and scans TCP ports from **50 to 84** to identify ports that accept connections.

It uses Python's built-in `socket` module to test TCP connectivity and displays the open ports found during the scan.

## ✨ Features

- **Hostname Resolution:** Converts a hostname into an IPv4 address.
- **TCP Port Scanning:** Checks ports 50–84 for accepting TCP connections.
- **Open Port Detection:** Reports ports that accept connections.
- **Connection Timeout:** Uses a one-second connection timeout.
- **Error Handling:** Handles hostname resolution errors, connection errors, and keyboard interruption.
- **Scan Information:** Displays the target and scan start time.

## 🛠️ Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking

## 📂 Project Structure

```text
python-port-scanner/
├── scanner.py
└── README.md
```

## ⚙️ Requirements

- Python 3 installed on your system.
- Network access to the authorized target.

No external Python packages are required.

## 🚀 Installation and Usage

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Navigate to the project directory

```bash
cd python-port-scanner
```

### 3. Run the scanner

```bash
python3 scanner.py <IP_ADDRESS_OR_HOSTNAME>
```

Example:

```bash
python3 scanner.py 192.168.1.1
```

Replace the example IP address with a target you own or have explicit permission to test.

## 📊 Example Output

```text
**************************************************
Scanning Target: 192.168.1.1
Time Started: 2026-10-21 19:30:00
**************************************************
Checking ports
port 80 is open
port 443 is open
```

*Example output for illustration only; actual results depend on the target and network.*

## 🎯 Learning Objectives

- Understand TCP connections and port numbers.
- Learn Python socket programming.
- Explore how open ports can be identified.
- Practice basic network troubleshooting and error handling.
- Develop foundational skills in cybersecurity and ethical hacking.

## ⚠️ Limitations

- Scans only ports 50–84.
- Uses sequential scanning, so each port is checked individually.
- Reports ports that accept TCP connections; it does not identify the services or versions running on them.
- Results may be affected by firewalls, filtering, network conditions, and connection timeouts.

## 🔒 Ethical Use

Use this tool only on systems you own or have explicit permission to test. Unauthorized port scanning may violate organizational policies or applicable laws.

## 👨‍💻 Author

**Venura Lakruwan**

Interested in cybersecurity, Python programming, networking, and ethical hacking.

---

⭐ If you find this project useful for learning, consider starring the repository.
