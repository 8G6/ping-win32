import os
p=os.popen('ipconfig | findstr IPv4 ').read().strip("\n").split(':')
print('IPv4 Adress :'+p[2])
os.system('ping '+p[2]+' -t')
