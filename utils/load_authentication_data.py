import json

def load_authentication_data():
    """
    Function to load authentication data (username and password) from a JSON file.
    
    Returns:
        dict: A dictionary containing the username and password loaded from the file.
              Example: {"username": "user", "password": "pass"}
    """
    
    # Load authentication data from the JSON file
    with open("data/keys.txt", 'r') as file:
        dados = json.load(file)

    # Extract username and password from the loaded data
    username = dados["username"]
    password = dados["password"]

    # Return the authentication data as a dictionary
    return {"username": username, "password": password}