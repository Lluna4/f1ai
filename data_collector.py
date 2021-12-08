import socket
import struct
import csv
UDP_IP = "127.0.0.1"
UDP_PORT = 20777
datt = ""
b = 0
sock = socket.socket(socket.AF_INET, # Internet
              socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, address= sock.recvfrom(4096)
    header = struct.unpack('<HBBBBQfIBB', data[:24])
    
    #print(header)
    
    if header[4] == 2:
        ggg = (data[0+i:21+i] for i in range(0, len(data), 21))

        for i in ggg:
            b += 1
            if b == 38:

                a = struct.unpack('<B32B32B16B16ffBBBBBBBBBBBBBBB16B16B', i) # car damage '<fBBBBBBBBBBBBBBBBB'
            
                print(a)
        b = 0
        with open('data1.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(a)
            csvfile.close()
        
            
        
        

        
        
    
    

    

