from scapy.all import sniff, ICMP, IP

def runner(substrate):
    if substrate.haslayer(ICMP):
        if substrate[IP].ttl==1:
            substrate.show()
            exit(0)

#waiting for incoming ICMP packets
sniff(prn=runner)
