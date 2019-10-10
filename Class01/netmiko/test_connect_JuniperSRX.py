from netmiko import ConnectHandler 
from getpass import getpass 

net_connect = ConnectHandler(
    host = 'srx2.lasthop.io', 
    username = 'pyclass', 
    password = getpass(), 
    device_type = 'juniper_junos',
    session_log='my_session_junos.txt',
)

print (net_connect.find_prompt())
