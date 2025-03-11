import json

def load_authentication_data():

    # Load authentication data
    with open("data/keys.txt", 'r') as file:
        dados = json.load(file)

    username = dados["username"]
    password = dados["password"]

    return {"username":username, "password":password }