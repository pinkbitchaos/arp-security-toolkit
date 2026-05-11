from scapy.all import sniff, ARP
from logger import log_alert

known_devices = {}

print("ARP Spoof Detector Started...\n")

def detect_spoof(packet):

    if packet.haslayer(ARP) and packet[ARP].op == 2:

        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        if ip in known_devices:

            if known_devices[ip] != mac:

                warning = (
                    f"[WARNING] POSSIBLE ARP SPOOFING DETECTED! "
                    f"IP: {ip} | OLD MAC: {known_devices[ip]} | NEW MAC: {mac}"
                )

                log_alert(warning)

        else:
            known_devices[ip] = mac

sniff(filter="arp", prn=detect_spoof, store=False)