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

interfaces = device.get_interfaces_ip()

for interface, details in interfaces.items():
    print(f'Interface: {interface}')
    for key, value in details.items():
        for ip, subnet in value.items():
            print(f'{key}: {ip}/{subnet['prefix_length']}')

device.close()