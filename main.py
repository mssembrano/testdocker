import os 
import subprocess
host = "0.0.0.0"
host1 = '8.8.8.8'
host2 = "8.8.8.4"
host3 = "192.168.1.1"
host4= "192.168.1.2"

def pingCheck(host): #With Pin
    response = os.system("ping -q " + host)
    if response == 0:
        print (host + " Reachable")
    else:
        print(host + " Unreachable")



def pingCh(host):
    with open(os.devnull, "wb") as limbo:
        response = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", host],
            stdout=limbo, stderr=limbo).wait()
        if response==0:
            print(host + " Reachable")
        else:
            print (host + " Unreachable")

pingCh(host1)
pingCh(host2)
pingCh(host3)
pingCh(host4)