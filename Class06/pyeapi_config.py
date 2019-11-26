import pyeapi
from getpass import getpass

#import ipdb
#ipdb.set_trace()

connection = pyeapi.client.connect(
    transport = "https",
    host = "arista1.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443",
)

cfg = [
    "vlan 125",
    "name han-green",
    "vlan 126",
    "name han-red",
]


device = pyeapi.client.Node(connection)
output = device.config(cfg)
print(output)
