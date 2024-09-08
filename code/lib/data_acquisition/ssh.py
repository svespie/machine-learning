import paramiko

class SSHConnection:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.__ssh_client = paramiko.SSHClient()
        self.__ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)  #remove for production
        self.__ssh_client.connect(hostname=self.host, username=self.username, password=self.password)

    def execute(self, command):
        _, stdout, _ = self.__ssh_client.exec_command(command)
        result = stdout.read()
        return result.decode("ascii")