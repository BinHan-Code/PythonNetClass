from netmiko import ConnectHandler 
from getpass import getpass 

device_cisco3 = {
   "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
    "global_delay_factor": 2, 
}

net_connect = ConnectHandler(**device_cisco3)
print (net_connect.find_prompt())

cfg = [
    'logging buffered 200000',
    'no logging console',
]
output = net_connect.send_config_set(cfg)
print(output)
