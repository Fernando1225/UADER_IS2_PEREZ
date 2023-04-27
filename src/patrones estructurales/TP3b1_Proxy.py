import subprocess

class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            for i in range(10):
                result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
                print(result.stdout.decode())
        else:
            print("Error: IP address does not start with '192.'")
    
    def executefree(self, ip):
        for i in range(10):
            result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
            print(result.stdout.decode())


class PingProxy:
    def __init__(self):
        self.ping = Ping()
    
    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)




ping = PingProxy()

user_input = str(input('Introduce the ip you want to connect to: '))

ping.execute(user_input)