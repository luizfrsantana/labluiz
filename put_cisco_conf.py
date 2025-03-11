from utils.connect_to_device_cisco import connect_to_device_cisco
import json

def configure_device_interfaces():
    """
    Function to read device information from a JSON file, generate interface configurations, 
    and apply them to Cisco devices.

    This function iterates over each device in the `devices.txt` file, generates configurations 
    for each interface (including description, IP address, and status), and applies the 
    configurations to the devices.

    Args:
        None: The function reads from a JSON file (`data/devices.txt`) that contains the 
              device configuration data.

    Returns:
        None: The function applies the configurations to the devices and handles exceptions if they occur.
    """
    try:
        # Open the file that contains device information and load it into a dictionary
        with open('data/devices.txt', 'r') as file:
            devices = json.load(file)

        # Iterate over each device in the devices list
        for device in devices:
            for hostname, data in device.items():
                config = ""  # Initialize an empty string for the configuration

                # Iterate over each interface in the 'interfaces' section of the device
                for interface, settings in data["interfaces"].items():

                    # Set the description and status for the interface
                    if not settings.get("description"):
                        description = "NO CONNECTION"  # Default if no description is provided
                        status = "shutdown"  # Disable the interface if no description is provided
                    else:
                        description = settings.get("description")  # Use the description from the data
                        status = "no shutdown"  # Enable the interface if description is provided

                    # Set the IP address configuration for the interface
                    ip = "no ip address" if not settings.get("ip_address") else "ip address " + settings.get("ip_address")

                    # Build the configuration string for the interface
                    config += f'''
                    interface {interface}
                        description {description}
                        {ip}
                        {status}
                    '''

                # Connect to the Cisco device and apply the configuration
                device_connection = connect_to_device_cisco(hostname)
                device_connection.open()  # Open the device connection

                # Merge the generated configuration into the device's candidate configuration
                device_connection.load_merge_candidate(config=config)

                # Commit the configuration to the device
                device_connection.commit_config()

                # Close the device connection
                device_connection.close()

    except Exception as e:
        return {"status": {e}} 
    
    return {"status": "success"}

print(configure_device_interfaces())
