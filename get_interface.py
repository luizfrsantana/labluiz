from napalm import get_network_driver
import json

with open("data/keys.txt", 'r') as file:
    dados = json.load(file)

print("Device IP Informations")
hostname = "192.168.56.1" + input("Device IP - 192.168.56.1X: ")
username = dados["username"]
password = dados["password"]

driver = get_network_driver("ios")

device = driver(hostname=hostname, username=username, password=password)

device.open()

interface_ips = device.get_interfaces_ip()
interfaces_info = device.get_interfaces()
clear_interface_data = []

for interface_name, details in interface_ips.items():
    interface_data = {interface_name: {}}
    interface_data[interface_name]["description"] = interfaces_info[interface_name]['description']
    interface_data[interface_name]["up"] = interfaces_info[interface_name]['is_up']
    interface_data[interface_name]["enable"] = interfaces_info[interface_name]['is_enabled']

    for key, value in details.items():
        interface_data[interface_name][key] = {}

        for ip, subnet in value.items():
            interface_data[interface_name][key][ip] = subnet['prefix_length']
        
    clear_interface_data.append(interface_data)

print(clear_interface_data)

device.close()