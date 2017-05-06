import os 

response = os.system("ping -c 2 8.8.8.8")


if response == 0:
    print ("Active Account!")
elif response ==256:
    print("Account Deactivated")
else:
    print("Hu U")