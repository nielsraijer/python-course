#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

hosts = [ "cisco1.lasthop.io", "cisco2.lasthop.io" ]
username = "pyclass"
device_type= "cisco_nxos"

for host in hosts:
    net_connect = ConnectHandler(
        host=host, 
        username=username,
        password=getpass(), 
        device_type=device_type
        )

    print(net_connect.find_prompt())


