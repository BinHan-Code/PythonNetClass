from netmiko import ConnectHandler 
from getpass import getpass 

device_cisco3 = {
   "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**device_cisco3)
print (net_connect.find_prompt())

output = net_connect.send_command("show ip int brief", use_textfsm=True)
print(output)

net_connect.disconnect()
