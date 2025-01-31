[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17893398)
# IP Freely
This is a simple Python script that scans a network range specified in CIDR notation and checks which IP addresses are active (UP) or inactive (DOWN) by sending ping requests.
## Features
- Scans a network range provided in CIDR notation (e.g., 192.168.1.0/24).

- Detects active hosts by sending a single ping request to each IP address.

- Works on both Windows and Linux/macOS systems.

- Displays a summary of active and inactive hosts after the scan.
## Requirements
- Makes sure you have `Python3` installed
- Operating system: `Windows, Linux, or macOS`
## Usage
Run the script:
```bash
python3 scan.py <CIDR>
```
**Example:**
```bash
python3 scan.py 10.103.0.58/24
```
## Error Handling
### Invalid CIDR Notation:
- If the CIDR notation is not in the correct format (ex: missing `/`), the script will display an error message.
### Invalid Prefix
- If the prefix is not a number or outside the valid range (0 to 32), the script will display an error message.

## Script in Action
![](scan.gif)