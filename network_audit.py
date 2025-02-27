import nmap
import socket

def scan_network(network_range):
    """Σαρώνει το τοπικό δίκτυο και εντοπίζει ενεργές συσκευές"""
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network_range, arguments="-sn")  # Ping scan για εύρεση συσκευών

    devices = []
    for host in scanner.all_hosts():
        hostname = socket.getfqdn(host)  # Ανάκτηση hostname
        devices.append((host, hostname))
    
    return devices

def scan_ports(target_ip):
    """Ελέγχει ανοιχτές θύρες σε μια συγκεκριμένη IP"""
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, arguments="-T4 -F")  # Γρήγορη σάρωση θυρών
    
    open_ports = []
    for port in scanner[target_ip]['tcp']:
        if scanner[target_ip]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    
    return open_ports

def generate_report(devices):
    """Δημιουργεί ένα report με τις ενεργές συσκευές και τις ανοιχτές θύρες"""
    with open("network_audit.txt", "w") as report:
        report.write(" Basic Network Security Audit Report\n")
        report.write("="*40 + "\n")
        for ip, hostname in devices:
            report.write(f"\n Device: {hostname} ({ip})\n")
            open_ports = scan_ports(ip)
            if open_ports:
                report.write(f" Open Ports: {', '.join(map(str, open_ports))}\n")
            else:
                report.write(" No open ports detected.\n")
        report.write("\n Audit Complete!\n")
    
    print("\n Report saved as 'network_audit.txt'")

if __name__ == "__main__":
    network_range = input("Enter the network range to scan (e.g., 192.168.1.0/24): ")
    print("\n Scanning network...")
    active_devices = scan_network(network_range)

    if active_devices:
        print(f"\n Found {len(active_devices)} active devices. Generating report...")
        generate_report(active_devices)
    else:
        print("\n No active devices found.")
