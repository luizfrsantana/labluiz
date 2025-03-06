from napalm import get_network_driver
import time
import json

with open("keys.txt", 'r') as file:
    dados = json.load(file)

print("GET Device IP Informations")
hostname = "192.168.56.1" + input("Device IP - 192.168.56.1X: ")
ping_destination = input("IP Destination: ")
username = dados["username"]
password = dados["password"]

timeout_seconds = 30

driver = get_network_driver("ios")

device = driver(hostname=hostname, username=username, password=password)

device.open()

start_time = time.time()

result = device.ping(ping_destination)

success = result['success']
packet_loss = success['packet_loss']

if packet_loss > 0:
    print(f"Perda de pacotes: {packet_loss}%")
else:
    print("Nenhuma perda de pacotes.")

print("Ping bem-sucedido!" if packet_loss == 0 else "Ping falhou.")

device.close()