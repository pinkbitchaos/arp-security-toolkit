from scapy.all import ARP, Ether, srp

target_ip = "192.168.229.1/24"

print("\nScanning network...\n")

arp = ARP(pdst=target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

result = srp(packet, timeout=5, verbose=0)[0]

print("IP ADDRESS\t\tMAC ADDRESS")
print("-" * 50)

found = False

for sent, received in result:

    found = True

    print(f"{received.psrc}\t\t{received.hwsrc}")

if not found:
    print("\nNo devices found.")