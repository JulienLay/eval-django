from scapy.all import *
listIPCapture=[]
try :
    f=open('capture_stat_ip.csv','r')
    listIP=f.readlines()
    f.close()
except Exception:
    listIP=[]
for i in range(0,len(listIP)):
    if(listIP[i][-1]=='\n'):
        listIP[i]=listIP[i][:-1]

def saveIP(packet) :
    f=open('capture_stat_ip.csv','a')
    if(packet[IP].src not in listIP):
        listIP.append(packet[IP].src)
        f.write(packet[IP].src+'\n')
    if(packet[IP].dst not in listIP):
        listIP.append(packet[IP].dst)
        f.write(packet[IP].dst+'\n')
    f.close()
sniff(count=0,iface=dev_from_index(2),filter='ip',prn=saveIP)
