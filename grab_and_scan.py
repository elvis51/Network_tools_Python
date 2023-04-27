
from port_scanner import Scanner
from grabber import Grabber



def main():
    ip = ''
    portrange = (1, 100)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error", e)


if __name__ == '__main__':
    main()
