import socket

def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            return True
        else:
            return False
        sock.close()

    except KeyboardInterrupt:
        print("Ctrl+C pressed. Exiting...")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting...")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server. Exiting...")
        sys.exit()

def scan(ip_address):
    for port in range(1, 1025):
        if scan_port(ip_address, port):
            print(f"Port {port} is open.")

def main():
    ip_address = input("Enter the IP address: ")
    scan(ip_address)

if __name__ == "__main__":
    main()