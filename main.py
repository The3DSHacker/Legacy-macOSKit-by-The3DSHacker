import subprocess
import sys

def restart_normal():
    print("Standard rebooting...")
    subprocess.run("sudo shutdown -r now", shell=True, check=True)

def shutdown_mac():
    print("Turning off...")
    subprocess.run("sudo shutdown -h now", shell=True, check=True)

def restart_recovery():
    print("Rebooting in recovery mode...")
    subprocess.run("sudo nvram recovery-boot-mode=unused", shell=True, check=True)
    subprocess.run("sudo shutdown -r now", shell=True, check=True)

def restart_internet_recovery():
    print("Rebooting in Internet recovery...")
    subprocess.run("sudo nvram internet-recovery-mode=RecoveryModeDisk", shell=True, check=True)
    subprocess.run("sudo shutdown -r now", shell=True, check=True)

def clear_nvram():
    print("Resetting nvram variables...")
    subprocess.run("sudo nvram -c", shell=True, check=True)

def open_recovery_terminal():
    print("The terminal of the recovery mode can't be used in Normal macOS.\n"
          "You need to access recovery mode and launch Terminal manually.")

def menu():
    while True:
        print("\n--- Legacy macOSKit by The3DSHacker ---")
        print("1. Standard reboot")
        print("2. Reboot in recovery mode")
        print("3. Reboot in Internet Recovery")
        print("4. Turn off the Mac")
        print("5. Open terminal in recovery mode (manual)")
        print("6. Reset the nvram variables")
        print("0. Quit")
        choix = input("Select an option : ")
        if choix == "1":
            restart_normal()
            break
        elif choix == "2":
            restart_recovery()
            break
        elif choix == "3":
            restart_internet_recovery()
            break
        elif choix == "4":
            shutdown_mac()
            break
        elif choix == "5":
            open_recovery_terminal()
        elif choix == "6":
            clear_nvram()
        elif choix == "0":
            print("Goodbye.")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()