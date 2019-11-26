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

device = pyeapi.client.Node(connection)
output = device.enable("show version")
print(output)
