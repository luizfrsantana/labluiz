# Import the function to connect to a Cisco device
from connect_to_device_cisco import connect_to_device_cisco

def get_ping(hostname, ping_destination):
    """
    Function to perform a ping operation on a Cisco device and retrieve the results.
    
    Args:
        hostname (str): The IP address or hostname of the Cisco device.
        ping_destination (str): The IP address or hostname to ping from the device.
    
    Returns:
        None: The function prints the ping results and handles exceptions if they occur.
    """
    # Establish connection to the Cisco device
    device = connect_to_device_cisco(hostname)
    device.open()

    try:
        # Execute the ping command on the device to the specified destination
        ping_result = device.ping(ping_destination)

        # Print ping results for each key in the result
        for key, details in ping_result.items():
            sanitize_ping_data = {"destination":ping_destination, "result": key, "packets_sent": details["probes_sent"], "packets_loss": details["packet_loss"]}

    except Exception as e:
        # Handle errors during the ping operation
        print(f"Error during ping operation: {e}") 

    # Close the connection to the device and return data
    device.close()
    return sanitize_ping_data
    
# Inform the user that the device IP information is being retrieved
print("GET Device IP Informations")
hostname = "192.168.56.1" + input("Device IP - 192.168.56.1X: ")
ping_destination = input("IP Destination: ")
print(get_ping(hostname, ping_destination))