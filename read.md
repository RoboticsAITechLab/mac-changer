# Advanced MAC Address Changer

## Description
This script allows users to change their MAC address dynamically with security key protection. It ensures safe usage and prevents unauthorized access. Additionally, it supports automatic MAC address rotation at user-defined intervals.

## Features
- **Security Key Protection**: Only authorized users can run the script.
- **Automatic MAC Rotation**: Change MAC addresses at regular intervals.
- **Interface Detection**: Automatically detects the active network interface.
- **MAC Reset**: Reset to the original MAC address when needed.
- **Logging**: Logs all MAC address changes for security tracking.

## Installation

### Requirements
Ensure you have the following installed:
- Python 3.x
- `macchanger` (install using `sudo apt install macchanger` on Debian-based systems)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mac-changer.git
   cd mac-changer
   ```
2. Install required dependencies:
   ```sh
   sudo apt install macchanger
   ```
3. Run the setup process:
   ```sh
   python3 mac_changer.py
   ```
4. Create your security key during the setup process.

## Usage
1. Run the script:
   ```sh
   sudo python3 mac_changer.py
   ```
2. Enter your security key when prompted.
3. Choose an option from the menu:
   - **Start MAC Changer**: Changes MAC address dynamically.
   - **Disable MAC Changer Service**: Stops automatic changes.
   - **Reset MAC Address**: Restores the original MAC.
   - **Exit**: Closes the program.

## Security Key System
- The first time you run the script, you'll be asked to set up a security key.
- This key is required for future usage to prevent unauthorized access.
- If you forget the key, you must delete the `security.key` file and set up a new one.

## Resetting MAC Address
To reset your MAC address back to the original:
```sh
sudo python3 mac_changer.py
```
Then select the **Reset MAC Address** option from the menu.

## Logging
All changes are logged in `mac_changer.log` for security tracking. You can review logs using:
```sh
cat mac_changer.log
```

## Disclaimer
This tool is for educational purposes only. The author is not responsible for any misuse.

## License
This project is licensed under the MIT License.

