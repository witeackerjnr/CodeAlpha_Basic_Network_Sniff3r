from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("Starting packet sniffer...")
    # Start sniffing packets
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
