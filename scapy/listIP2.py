from scapy.all import *
nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
show_interfaces()
indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
packets=sniff(count=nbPackets,iface=dev_from_index(indexCarte))
fluxIP={}
for packet in packets :
    if packet.haslayer(IP) :
        if packet[IP].src not in fluxIP :
            fluxIP[packet[IP].src]=packet[IP].dst

for srcIP in fluxIP:
    print(srcIP+"->"+fluxIP[srcIP])
