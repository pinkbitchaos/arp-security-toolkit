import os

while True:

    print("""
================================
      ARP SECURITY TOOLKIT
================================

1. Network Scanner
2. ARP Packet Sniffer
3. ARP Spoof Detector
4. Exit

================================
""")

    choice = input("Select an option: ")

    if choice == "1":
        os.system("python scanner.py")

    elif choice == "2":
        os.system("python sniffer.py")

    elif choice == "3":
        os.system("python detector.py")

    elif choice == "4":
        print("Exiting toolkit...")
        break

    else:
        print("Invalid option. Try again.")