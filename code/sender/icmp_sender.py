from scapy.all import IP, ICMP, send

ip_component = IP()
ip_component.ttl = 1
ip_component.dst = "receiver"
icmp_component = ICMP()
unified_components = ip_component/icmp_component
send(unified_components)



