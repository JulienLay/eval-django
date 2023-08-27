from scapy.all import *
listIP=[]
show_interfaces()
indexCarte=int(input('Quel est l\'index de la carte à capturer  ?'))
def countIP(packet):
    if packet.haslayer(IP):
        if(packet[IP].src not in listIP):
            listIP.append(packet[IP].src)
        if(packet[IP].dst not in listIP):
            listIP.append(packet[IP].dst)
packets=sniff(iface=dev_from_index(indexCarte),prn=countIP)
print(listIP)
