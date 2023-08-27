from scapy.all import *
nbPackets=int(input('Combien de paquet souhaitez-vous sniffer ?'))
show_interfaces()
indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
packets=sniff(iface=dev_from_index(indexCarte))
listeIP=[]
for packet in packets :
    if packet.haslayer(IP) :
        if packet[IP].src not in listeIP :
            listeIP.append(packet[IP].src)
        if packet[IP].dst not in listeIP :            
            listeIP.append(packet[IP].dst)

f=open('capture_stat_ip.csv','w')
for ip in listeIP:
        f.write(ip+'\n')
f.close()
