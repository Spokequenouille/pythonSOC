import nmap

service_scan = {
    "web": ["192.168.1.1", "80,443", ""],
    "bdd": ["192.168.1.1", "3306", ""],
    "sg":  ["192.168.1.1", "", ""]
}

def scanner():
    pass


if __name__ == "__main__":
    for service in service_scan:
        print(service)