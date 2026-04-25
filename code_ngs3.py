from netmiko import ConnectHandler 
import getpass
password = getpass.getpass()
command = ['show ip int br', 'show vlan']
device = {
    'device_type' : 'cisco_ios',
    'host': ' 192.168.122.42',
    'username': 'saja',
    'password': password
}

net_connect = ConnectHandler(**device)
for cmd in command:
    out = net_connect.send_command(cmd)
    print (out)


##### Output

# root@NetworkAutomation-1:~# python3 ssh
# /usr/local/lib/python3.8/dist-packages/paramiko/transport.py:32: CryptographyDeprecationWarning: Python 3.8 is no longer supported by the Python core team and support for it is deprecated in cryptography. The next release of cryptography will remove support for Python 3.8.
#   from cryptography.hazmat.backends import default_backend
# Password:
# Interface              IP-Address      OK? Method Status                Protocol
# GigabitEthernet0/0     unassigned      YES unset  up                    up
# GigabitEthernet0/1     unassigned      YES unset  up                    up
# GigabitEthernet0/2     unassigned      YES unset  down                  down
# GigabitEthernet0/3     unassigned      YES unset  down                  down
# GigabitEthernet1/0     unassigned      YES unset  down                  down
# GigabitEthernet1/1     unassigned      YES unset  down                  down
# GigabitEthernet1/2     unassigned      YES unset  down                  down
# GigabitEthernet1/3     unassigned      YES unset  down                  down
# GigabitEthernet2/0     unassigned      YES unset  down                  down
# GigabitEthernet2/1     unassigned      YES unset  down                  down
# GigabitEthernet2/2     unassigned      YES unset  down                  down
# GigabitEthernet2/3     unassigned      YES unset  down                  down
# GigabitEthernet3/0     unassigned      YES unset  down                  down
# GigabitEthernet3/1     unassigned      YES unset  down                  down
# GigabitEthernet3/2     unassigned      YES unset  down                  down
# GigabitEthernet3/3     unassigned      YES unset  down                  down
# Vlan1                  192.168.122.42  YES manual up                    up

# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/0, Gi0/1, Gi0/2, Gi0/3, Gi1/0, Gi1/1, Gi1/2, Gi1/3, Gi2/0, Gi2/1, Gi2/2, Gi2/3, Gi3/0, Gi3/1, Gi3/2, Gi3/3
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup

# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

# Remote SPAN VLANs
# ------------------------------------------------------------------------------


# Primary Secondary Type              Ports
# ------- --------- ----------------- ------------------------------------------

# root@NetworkAutomation-1:~#

