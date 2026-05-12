# ARP Security Toolkit

## Description

ARP Security Toolkit is a Python-based cybersecurity project designed to demonstrate how ARP (Address Resolution Protocol) works, how ARP spoofing attacks can affect local networks, and how suspicious ARP behavior can be detected using defensive monitoring techniques.

This project was built for educational and ethical cybersecurity learning purposes.

---

## Features

* Network Device Scanner
* Live ARP Packet Sniffer
* ARP Spoof Detection
* Alert Logging System
* Real-Time Network Monitoring
* IP and MAC Address Discovery

---

## Technologies Used

* Python
* Scapy
* Npcap

---

## Project Structure

```text
arp-security-toolkit/
│
├── scanner.py
├── sniffer.py
├── detector.py
├── logger.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pinkbitchaos/arp-security-toolkit.git
```

Move into the project folder:

```bash
cd arp-security-toolkit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Npcap for Windows:

[https://npcap.com/](https://npcap.com/)

During installation enable:

* Install Npcap in WinPcap API-compatible Mode

---

## Usage

### Run Network Scanner 

```bash
python scanner.py
```

### Run ARP Sniffer

```bash
python sniffer.py
```

### Run ARP Spoof Detector

```bash
python detector.py
```

---

## Example Detection Output

```text
[WARNING] POSSIBLE ARP SPOOFING DETECTED!
IP: 192.168.1.1
OLD MAC: AA:BB:CC:11:22:33
NEW MAC: FF:EE:DD:44:55:66
```

---

## Author

vicious