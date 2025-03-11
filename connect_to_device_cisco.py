from napalm import get_network_driver
from load_authentication_data import load_authentication_data

def connect_to_device_cisco(hostname):
    # Define the driver for the device
    driver = get_network_driver("ios")

    # Connect to the device
    device = driver(hostname=hostname, username=load_authentication_data()["username"], password=load_authentication_data()["password"])

    return device