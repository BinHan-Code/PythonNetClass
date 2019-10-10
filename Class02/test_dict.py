from netmiko import ConnectHandler 
from getpass import getpass 

device_cisco3 = {
   "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
    "session_log": 'my_session_part1.txt',
}

net_connect = ConnectHandler(**device_cisco3)
print (net_connect.find_prompt())

command = 'delete flash:/cisco3-cfg-Oct--5-17-54-26.295-2'
output = net_connect.send_command_timing(command, 
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('y',
    strip_prompt=False, strip_command=False)
print(output)


