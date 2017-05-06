import os 

response1 = os.system("ping -c 1 8.8.8.8")
response2 = os.system("ping -c 1 8.8.8.4")
response3 = os.system("ping -c 1 192.168.1.1")
response4 = os.system("ping -c 1 192.168.1.2")


if response1 == 0:
    print ("8.8.8.8 Reachable")
elif response1 ==256:
    print ("8.8.8.8 Unreachable")

if response2 == 0:
    print ("8.8.8.4 Reachable ")
elif response2 ==256:
    print ("8.8.8.4 Unreachable ")

if response3 == 0:
    print ("192.168.1.1 Reachable ")
elif response3 ==256:
    print ("192.168.1.1 Ureachable ")

if response4 == 0:
    print ("192.168.1.2 Reachable")
elif response4 ==256:
    print ("192.168.1.2 Ureachable ")