from napalm import get_network_driver
import json

with open("data/keys.txt", 'r') as file:
    keys = json.load(file)

username = keys['username']
password = keys['password']

with open('data/devices.txt', 'r') as file:
    devices = json.load(file)

driver = get_network_driver('ios')

for device in devices:
    for hostname, data in device.items():
        interfaces = data["interfaces"]
        config = ""
        for interface, settings in interfaces.items():

            if not settings.get("description"):
                description = "NO CONECTION"
                status = "shutdown"
            else:
                description = "description " + settings.get("description")
                status = "no shutdown"

            ip = "no ip address" if not settings.get("ip_address") else "ip address " + settings.get("ip_address")

            config += f'''
            interface {interface}
                description {description}
                {ip}
                {status}
            '''

        device = driver(hostname=hostname, username=username, password=password)
        device.open()
        device.load_merge_candidate(config=config)
        
        device.commit_config()
        device.close()



