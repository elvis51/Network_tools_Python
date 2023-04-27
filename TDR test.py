import netmiko
from netmiko import ConnectHandler
import time
import base64

cisco = {
    'device_type': 'cisco_ios',
    'ip':   input("enter switch ip address:"),
    'username':base64.b64decode("").decode("utf-8"),
    'password':base64.b64decode("").decode("utf-8"),
}
net_connect =ConnectHandler(**cisco)
net_connect.enable()
def tdr_test():
    int = input("enter interface name(Gi*/*/*): ")
    tdr_req =net_connect.send_command('test cable-diagnostics tdr int ' + int )
    print("TDR test started on interface", int )
    time.sleep(15)
    tdr_ans =net_connect.send_command('show cable-diagnostics tdr int ' + int)
    print(tdr_ans)
    error_ans =net_connect.send_command('show interfaces' + int, ' counters errors')
    print(error_ans)
    restart = input ("Do you want ot test again(yes/no): ")
    if restart == "yes":
        tdr_test()
    else:
        print('Closing Connection')
        net_connect.disconnect()
        exit()
tdr_test()

