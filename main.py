import json
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def load_user_info_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def create_ftp_server(user_info):
    authorizer = DummyAuthorizer()

    for user_data in user_info:
        username = user_data["username"]
        password = user_data["password"]
        path = user_data["path"]
        permissions = user_data["permissions"]

        authorizer.add_user(username, password, path, perm=permissions)

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    user_info = load_user_info_from_json("ftp_config.json")
    create_ftp_server(user_info)
