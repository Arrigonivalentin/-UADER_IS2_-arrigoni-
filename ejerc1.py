import os

class Ping:
    def execute(self, ip: str):
        if not ip.startswith("192."):
            raise ValueError("Dirección IP no permitida. Debe comenzar con '192.'")
        print(f"[Ping] Realizando ping a {ip}...")
        os.system(f"ping -c 10 {ip}")

    def executefree(self, ip: str):
        print(f"[Ping] Realizando ping libre a {ip}...")
        os.system(f"ping -c 10 {ip}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("[PingProxy] Dirección especial detectada. Enviando ping a www.google.com con método libre.")
            self.ping.executefree("www.google.com")
        else:
            print(f"[PingProxy] Redirigiendo a Ping.execute para la IP: {ip}")
            self.ping.execute(ip)
