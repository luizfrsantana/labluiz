from napalm import get_network_driver
from utils.load_authentication_data import load_authentication_data

def connect_to_device_cisco(hostname):
    """
    Function to connect to a Cisco device using the NAPALM library.
    
    Args:
        hostname (str): The IP address or hostname of the Cisco device.
    
    Returns:
        device: A device object representing the connection to the Cisco device.
                This object can be used to execute commands and retrieve information.
    """
    
    # Define the driver for the device
    driver = get_network_driver("ios")

    # Connect to the device using the provided hostname and authentication data
    device = driver(hostname=hostname, username=load_authentication_data()["username"], password=load_authentication_data()["password"])

    # Return the device connection object
    return device