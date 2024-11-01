from scapy.all import sniff
def packet_callback(packet):
    print(packet.summary()) 
sniff(prn=packet_callback, count=300)



