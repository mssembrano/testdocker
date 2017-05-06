import os 
import subprocess

def pingCh(host):
    with open(os.devnull, "wb") as limbo:
        response = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", host],
            stdout=limbo, stderr=limbo).wait()
        if response==0:
            print(host + " Reachable")
        else:
            print (host + " Unreachable")

pingCh("8.8.8.8")
pingCh("8.8.8.4")
pingCh("192.168.1.1")
pingCh("192.168.1.2")

list1 = [1,2,3]

for x in range(0,3):
    print (list1[x])
    
