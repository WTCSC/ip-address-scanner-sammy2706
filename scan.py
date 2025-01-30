import sys  # For handling command-line arguments
import os   # For running ping commands

# Check if the user provided a CIDR notation as input
if len(sys.argv) != 2:
    print("Usage: python3 scan.py <CIDR>")
    sys.exit(1)

cidr = sys.argv[1]  # Get the CIDR from command line

# Split the CIDR into the network and prefix
try:
    network, prefix = cidr.split('/')
except ValueError:
    print("Invalid CIDR notation. Use format like '192.168.1.0/24'.")
    sys.exit(1)

# Check if the prefix is valid
try:
    prefix = int(prefix)
    if prefix < 0 or prefix > 32:
        print("Prefix must be between 0 and 32.")
        sys.exit(1)
except ValueError:
    print("Prefix must be a number.")
    sys.exit(1)

# Print the network being scanned
print(f"Scanning network {cidr}...\n")

# Counters for tracking host statuses
net_id = []
available_hosts = 2 ** (32 - prefix) - 1
up_count = 0
down_count = 0
network = network.split('.')  
while prefix >= 8:
    prefix -= 8
    net_id.append(network.pop(0))
if prefix > 0:
    net_id.append(int(network.pop(0)) & (255 << (8 - prefix)))
while network:
    net_id.append(network.pop(0))
ip = [int(i) for i in net_id]

# Iterate over all possible IPs in the range
for i in range(available_hosts):
    ip[3] += 1
    for j in range(3, 0, -1):
        if ip[j] > 255:
            ip[j] = 0
            ip[j-1] += 1
    ip_str = '.'.join([str(i) for i in ip])

    # Ping the IP address
    if os.name == "nt":  # Windows
        command = f"ping -n 1 -w 1000 {ip_str}"
    else:  # Linux/macOS
        command = f"ping -c 1 -W 1 {ip_str}"

    # Run the ping command
    response = os.system(command)

    # Check if the ping was successful
    if response == 0:
        print(f"{ip_str:15} - UP")
        up_count += 1
    else:
        print(f"{ip_str:15} - DOWN")
        down_count += 1

# Print summary of the scan results
print(f"\nScan complete. Found {up_count} active hosts, {down_count} down.")