import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format = "jsonrpc",
    host = "nxos1.lasthop.io",
    username = "pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False,
)


#cmds = [
#    "show hostname",
#    "show version",
#    "show lldp neighbors",
#]

cfg_cmd = ["logging monitor 2"]
output = device.config_list(cfg_cmd)
print(output)

