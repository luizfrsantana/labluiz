from napalm import get_network_driver
import json

def get_device_interface_info(hostname):
    """
    Function to retrieve network interface information from a device.
    
    Args:
        hostname (str): The IP address or hostname of the device.
    
    Returns:
        list: A list containing dictionaries with interface information.
    """
    # Load authentication data
    with open("data/keys.txt", 'r') as file:
        dados = json.load(file)

    username = dados["username"]
    password = dados["password"]

    # Define the driver for the device
    driver = get_network_driver("ios")

    # Connect to the device
    device = driver(hostname=hostname, username=username, password=password)
    device.open()

    # Get IP information of interfaces and details
    interface_ips = device.get_interfaces_ip()
    interfaces_info = device.get_interfaces()
    clear_interface_data = []

    # Process interface data
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
    
    # Close the connection with the device
    device.close()
    
    return clear_interface_data

# Example of how to call the function in another code:
hostname = "192.168.56.1" + input("Device IP - 192.168.56.1X: ")
device_info = get_device_interface_info(hostname)

print(device_info)

    