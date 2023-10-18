# Simple Python FTP Server

This script creates an FTP server that allows users to connect and transfer files. The server is configured using a JSON file that contains user information, including usernames, passwords, directories, and permissions.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip: `pip install -r requirements.txt`

## Usage

1. Edit the `ftp_config.json` file to add or modify user information.
2. Run the script using Python: `python main.py`
3. Connect to the FTP server using an FTP client, such as FileZilla or WinSCP.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python installed on your system.
- The pyftpdlib library. You can install it using `pip`:

  ```bash
  pip install pyftpdlib



## Configuration

The `ftp_config.json` file contains an array of user objects, each with the following properties:

- `username`: The username for the user.
- `password`: The password for the user.
- `path`: The directory that the user has access to.
- `permissions`: The permissions that the user has, represented as a string of letters. For example, "elradfmw" represents all permissions.

## Acknowledgments

pyftpdlib: The Python library used for creating the FTP server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
