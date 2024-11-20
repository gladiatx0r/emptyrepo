import os
import platform
import getpass

def get_system_info():
    os_name = platform.system()  # e.g. Linux, Windows, Darwin (macOS)
    os_version = platform.version()  # Get the OS build/version
    username = getpass.getuser()  # More reliable way to get the current username
    return os_name, os_version, username

def main():
    os_name, os_version, username = get_system_info()
    
    print(f"Operating System: {os_name}")
    print(f"OS Version/Build: {os_version}")
    print(f"Current Username: {username}")
    
    # Conditional branches for OS-specific code
    if os_name == "Windows":
        print("Additional Windows-specific code can go here.")
        # Add Windows-specific code here
        
    elif os_name == "Linux":
        print("Additional Linux-specific code can go here.")
        # Add Linux-specific code here
        
    elif os_name == "Darwin":  # macOS is identified as 'Darwin'
        print("Additional macOS-specific code can go here.")
        # Add macOS-specific code here

if __name__ == "__main__":
    main()
