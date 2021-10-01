from netmiko import Netmiko
from pysnmp.entity.rfc3413.oneliner import cmdgen
import sys
from SNMPTrapReceiver import start

SW2 = {
    'host': "10.0.3.35",
    'username': 'ciscoclass',
    'password': 'kage',
    'secret': 'class',
    'device_type': 'cisco_ios'
}
SW1 = {
    'host': "10.0.3.24",
    'username': 'ciscoclass',
    'password': 'kage',
    'secret': 'class',
    'device_type': 'cisco_ios'
}

net_conn = Netmiko(**SW1)


# start listening for traps
def catch_trap():
    start()


# Controlling the enable mode in the terminal so we dont have to check for all different states of the console
def enable(state):
    if net_conn.check_enable_mode() is True and state is False:
        if net_conn.check_config_mode() is True:
            net_conn.exit_config_mode()
        print("Enable is off")
        net_conn.exit_enable_mode()
    elif net_conn.check_enable_mode() is False and state is True:
        print("Enable is on")
        net_conn.enable()


# Controlling the config mode in the terminal so we dont have to check for all different states of the console
def config(state):
    if net_conn.check_enable_mode() is False:
        enable(True)
    if net_conn.check_config_mode() is True and state is False:
        net_conn.exit_config_mode()
    elif net_conn.check_config_mode() is False and state is True:
        net_conn.config_mode()


# Creates a new vlan
def set_vlan(vlan, name, ip, mask):
    config(True)
    config_commands = [f'interface vlan {vlan}', f'ip address {ip} {mask}', f'vlan {vlan}', f'name {name}', 'do wr']
    o = net_conn.send_config_set(config_commands)
    print(o)
    return o


# Vlan menu for console user
def menu_vlan():
    vlan = input("Interface vlan: ")
    name = input("Vlan name: ")
    ip = input("Vlan ip address: ")
    mask = input("Subnetmask: ")
    set_vlan(vlan, name, ip, mask)


# Main menu to gather all the different methods
def menu_main():
    choice = int(input("1.New vlan\n2.catch snmp traps"))
    if choice == 1:
        menu_vlan()
    elif choice == 2:
        catch_trap()


# Testing how try catch works in python
try:
    while True:
        menu_main()
except ValueError:
    print("Oops!", sys.exc_info()[0], "occurred.")
