import os
import subprocess
import time

def check_docker_installed():
    try:
        subprocess.run(["docker", "--version"], check=True)
        print("[+] Docker is installed.")
    except subprocess.CalledProcessError:
        print("[-] Docker is not installed. Please install Docker and try again.")
        exit(1)

def setup_environment():
    print("[*] Setting up the Virtual SOC Analyst Lab...")
    subprocess.run(["docker-compose", "up", "-d"])
    print("[+] Lab setup complete. Services are starting...")

def show_lab_services():
    print("\n[+] Lab Services Running:")
    subprocess.run(["docker", "ps"])

def print_dashboard_info():
    print("\n[+] Access the SOC Dashboard:")
    print("    Splunk: http://localhost:8000 (admin:changeme)")
    print("    TheHive: http://localhost:9000")
    print("    MISP: http://localhost:8080")
    print("    Suricata Logs: ./logs/suricata/")

def main():
    check_docker_installed()
    setup_environment()
    time.sleep(5)  # Give containers time to start
    show_lab_services()
    print_dashboard_info()

if __name__ == "__main__":
    main()
