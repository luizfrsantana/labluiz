from napalm import get_network_driver
import json
from netmiko import ConnectHandler

with open("keys.txt", 'r') as file:
    dados = json.load(file)

print("GET Device IP Informations")
hostname = "192.168.56.1" + input("Device IP - 192.168.56.1X: ")
ping_destination = input("IP Destination: ")
username = dados["username"]
password = dados["password"]


driver = get_network_driver("ios")

device = driver(hostname=hostname, username=username, password=password)
device.device = ConnectHandler(device_type='cisco_ios', host=hostname, username=username, password=password, session_log='session.log')

device.open()

try:

    ping_result = device.ping(ping_destination)

    for key, details in ping_result.items():
        print(f'Result: {key} - Packets sent: {details['probes_sent']} - Packets loss: {details['packet_loss']} ')

except Exception as e:

    print(f"Error during ping operation: {e}") 

device.close()