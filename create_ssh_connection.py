import paramiko


def main():
    ip = ''
    username = ''
    password = ''
    timeout = 5
    client_policy = paramiko.AutoAddPolicy()
    client = paramiko.SSHClient();
    client.set_missing_host_key_policy(client_policy)
    client.connect(ip, username=username, password=password, timeout=timeout)
    print(client)




if __name__ == '__main__':
    main()
