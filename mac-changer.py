import os
import time
import random
import re
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='mac_changer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_mac():
    """Generate a random MAC address with a realistic OUI prefix."""
    oui_prefix = ["00:1A:2B", "00:1B:3C", "00:1C:4D", "00:1D:5E", "00:1E:6F"]
    return random.choice(oui_prefix) + ":" + ":".join(["%02x" % random.randint(0, 255) for _ in range(3)])


def check_macchanger_installed():
    """Check if macchanger is installed on the system."""
    try:
        subprocess.check_output("which macchanger", shell=True)
    except subprocess.CalledProcessError:
        print("[!] macchanger is not installed. Install it using: sudo apt install macchanger")
        exit(1)


def get_active_interface():
    """Automatically detects the active network interface."""
    try:
        output = subprocess.check_output("ip link show", shell=True).decode()
        interfaces = re.findall(r'([a-zA-Z0-9]+): <.*?UP', output)
        return interfaces[0] if interfaces else "wlan0"
    except Exception as e:
        logging.error(f"Error detecting interface: {e}")
        return "wlan0"


def change_mac(interface, new_mac):
    logging.info(f"Changing MAC address of {interface} to {new_mac}")
    os.system(f"sudo ip link set dev {interface} down")
    os.system(f"sudo ip link set dev {interface} address {new_mac}")
    os.system(f"sudo ip link set dev {interface} up")


def get_current_mac(interface):
    try:
        output = subprocess.check_output(f"ip link show {interface}", shell=True).decode()
        mac_address = re.search(r'link/ether ([0-9a-fA-F:]{17})', output).group(1)
        return mac_address
    except Exception as e:
        logging.error(f"Error getting MAC address: {e}")
        return None


def main():
    if os.geteuid() != 0:
        print("[!] Run this script as root!")
        exit(1)

    check_macchanger_installed()
    interface = get_active_interface()
    logging.info("Starting Advanced MAC Changer Script")
    print(f"[+] Detected Interface: {interface}")

    interval = input("Enter MAC change interval in seconds (default 600): ")
    try:
        interval = int(interval)
    except ValueError:
        interval = 600

    while True:
        old_mac = get_current_mac(interface)
        new_mac = generate_mac()
        if old_mac == new_mac:
            logging.warning("Generated same MAC, retrying...")
            continue

        change_mac(interface, new_mac)
        logging.info(f"New MAC Address set: {new_mac}")
        print(f"[+] New MAC Address: {new_mac}")

        time.sleep(interval)  # Change MAC based on user interval


def disable_macchanger():
    logging.info("Disabling MAC Changer Service")
    os.system("sudo systemctl stop macchanger")
    os.system("sudo systemctl disable macchanger")
    print("[+] MAC Changer Service Disabled")


def interactive_mode():
    print("""
    [1] Start MAC Changer
    [2] Disable MAC Changer Service
    [3] Exit
    """)
    choice = input("Select an option: ")
    if choice == "1":
        main()
    elif choice == "2":
        disable_macchanger()
    elif choice == "3":
        exit()
    else:
        print("[!] Invalid option")


if __name__ == "__main__":
    try:
        interactive_mode()
    except KeyboardInterrupt:
        logging.info("MAC Changer script terminated by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
