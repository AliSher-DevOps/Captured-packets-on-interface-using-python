from scapy.all import *
 
import matplotlib.pyplot as plt
 
import argparse
 

 
parser = argparse.ArgumentParser(description='Live Traffic Examiner')
 
parser.add_argument('interface', help="en0", type=str)
 
parser.add_argument('--count', help="Capture X packets and exit", type=int)
 
args=parser.parse_args()
 
#Check to see if we are root, otherwise Scapy might not be able to listen
 
if 1 :
 
   print("Warning: Not running as root, packet listening may not work.")
 
   try:
 
       print("--Trying to listen on {}".format(args.interface))
 
       sniff(iface=args.interface,count=1)
 
       print("--Success!")
 
   except:
 
       print("--Failed!\nError: Unable to sniff packets, try again using sudo.")
 
       quit()
 
if args.count:
 
   print("Capturing {} packets on interface {} ".format(args.count, args.interface))
 
else:
 
   print("Capturing unlimited packets on interface {} \n--Press CTRL-C to exit".format(args.interface))
 
#Interactive Mode
 
plt.ion()
 
#Labels
 
plt.ylabel("Bytes")
 
plt.xlabel("Count")
 
plt.title("Real time Network Traffic")
 
plt.tight_layout()
 
#Empty list to hold bytes
 
yData=[]
 
i=0
 
#Listen indefinitely, or until we reach count
 
while i<= args.count:
 
   #Listen for 1 packet
 
   for pkt in sniff(iface=args.interface,count=1):
 
       try:
           print(pkt.len)
           if IP in pkt:
               #print(pkt[IP].src)
               print(pkt[IP].len)
               
               yData.append(pkt[IP].len)
 
               plt.plot(yData)
 
               #Pause and draw
 
               plt.pause(1)
 
               i+=1
 
               if args.count:
 
                   if i <= args.count:
 
                       quit()
 
       except KeyboardInterrupt:
 
           print("Captured {} packets on interface {} ".format(i, args.interface))
 
           quit()