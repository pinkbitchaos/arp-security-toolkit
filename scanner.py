from scapy.all import ARP, Ether, srp

#change this to match your local network 
target_ip = "192.168.1.0/24"

print("\nScanning network...\n")

arp = ARP(pdst=target_ip)

ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

result = srp(packet, timeout=5, verbose=False)[0]

if result:

    print("IP ADDRESS\t\tMAC ADDRESS")
    print("-" * 50)

    for sent, received in result:
        print(f"{received.psrc}\t\t{received.hwsrc}")

else:
    print("No devices found.")