from netmiko import ConnectHandler
from test_my_devices import rtr3, rtr4, API

net_connect = ConnectHandler(**rtr3)
print(net_connect.find_prompt())

print(API_KEY)
