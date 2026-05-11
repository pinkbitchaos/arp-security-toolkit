from scapy.all import sniff, ARP

print("Starting ARP monitor...\n")

def process_packet(packet):

    if packet.haslayer(ARP):

        if packet[ARP].op == 1:
            print(f"[REQUEST] Who has {packet[ARP].pdst}? Tell {packet[ARP].psrc}")

        elif packet[ARP].op == 2:
            print(f"[REPLY] {packet[ARP].psrc} is at {packet[ARP].hwsrc}")

sniff(filter="arp", prn=process_packet, store=False)