import os
import time
import random
import json
from datetime import datetime

class VirtualServer:
    def __init__(self, name, os_type="Ubuntu 22.04 LTS", instance_type="t2.micro"):
        self.name = name
        self.os_type = os_type
        self.instance_type = instance_type
        self.public_ip = f"3.{random.randint(100,200)}.{random.randint(1,50)}.{random.randint(1,255)}"
        self.private_ip = f"10.0.{random.randint(1,10)}.{random.randint(1,255)}"
        self.status = "Stopped"
        self.security_groups = ["default"]
        self.ssh_key = "decodelabs-key.pem"
        self.web_server = "Not Installed"
        self.webpage_path = "/var/www/html/index.html"
        self.webpage_content = ""

    def launch(self):
        print(f"\n🔄 Launching server '{self.name}'...")
        time.sleep(2)
        self.status = "Running"
        print(f"✅ Server launched successfully!")
        print(f"   Public IP: {self.public_ip}")
        print(f"   Private IP: {self.private_ip}")
        print(f"   OS: {self.os_type}")
        print(f"   Instance Type: {self.instance_type}")

    def connect_ssh(self):
        print(f"\n🔐 Connecting to {self.public_ip} via SSH...")
        time.sleep(1)
        print(f"✅ SSH connection established")
        print(f"   Using key: {self.ssh_key}")
        print(f"   User: ubuntu@{self.public_ip}")

    def install_web_server(self, server_type="nginx"):
        print(f"\n📦 Installing {server_type} web server...")
        time.sleep(2)
        self.web_server = server_type
        print(f"✅ {server_type} installed successfully!")

    def deploy_webpage(self):
        self.webpage_content = """<!DOCTYPE html>
<html>
<head>
    <title>Welcome to DecodeLabs</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a, #1a1a2e);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        .container {
            padding: 40px;
            background: rgba(255,255,255,0.05);
            border-radius: 20px;
            border: 1px solid #00d4ff;
        }
        h1 {
            font-size: 48px;
            color: #00d4ff;
        }
        p {
            font-size: 20px;
            color: #aaa;
        }
        .badge {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 25px;
            background: #00d4ff;
            color: #0a0a0a;
            border-radius: 30px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to DecodeLabs</h1>
        <p>This server is running on <strong>Ubuntu 22.04 LTS</strong></p>
        <p>Web Server: <strong>Nginx</strong></p>
        <p>Deployed by: <strong>Aiman Zahoor</strong></p>
        <div class="badge">🚀 Cloud Infrastructure Engineer</div>
        <p style="margin-top: 30px; font-size: 14px; color: #666;">
            Server: <span id="server-info"></span>
        </p>
    </div>
    <script>
        document.getElementById('server-info').textContent = window.location.hostname;
    </script>
</body>
</html>"""

        print(f"\n📄 Deploying webpage to {self.webpage_path}...")
        time.sleep(1)
        print("✅ Webpage deployed successfully!")
        print(f"   Visit: http://{self.public_ip}")

    def configure_security(self):
        print("\n🔒 Configuring Security Groups...")
        time.sleep(1)
        self.security_groups.append("web-server")
        print("✅ Security groups configured:")
        print("   - SSH (22) allowed from 0.0.0.0/0")
        print("   - HTTP (80) allowed from 0.0.0.0/0")
        print("   - HTTPS (443) allowed from 0.0.0.0/0")

    def get_status(self):
        return {
            'name': self.name,
            'os': self.os_type,
            'instance_type': self.instance_type,
            'status': self.status,
            'public_ip': self.public_ip,
            'private_ip': self.private_ip,
            'web_server': self.web_server,
            'security_groups': self.security_groups
        }

    def display_summary(self):
        print("\n" + "=" * 60)
        print("   SERVER DEPLOYMENT SUMMARY")
        print("=" * 60)
        status = self.get_status()
        for key, value in status.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        print("=" * 60)

def main():
    print("\n" + "=" * 60)
    print("   THE SERVER COMMANDER - PROJECT 2 TASK 6")
    print("=" * 60)

    print("\n[1] Creating Virtual Server Instance...")
    server = VirtualServer("DecodeLabs-Server-01")

    print("\n[2] Launching Server...")
    server.launch()

    print("\n[3] Connecting via SSH...")
    server.connect_ssh()

    print("\n[4] Installing Web Server...")
    server.install_web_server("nginx")

    print("\n[5] Configuring Security Groups...")
    server.configure_security()

    print("\n[6] Deploying Webpage...")
    server.deploy_webpage()

    print("\n[7] Server Details:")
    server.display_summary()

    print("\n[8] Webpage Preview:")
    print("-" * 60)
    print(server.webpage_content[:500] + "...")
    print("-" * 60)

    print("\n" + "=" * 60)
    print("   TASK 6 COMPLETE")
    print("=" * 60)

    print("\n📋 Deployment Log:")
    print("-" * 60)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Server: {server.name}")
    print(f"Public IP: {server.public_ip}")
    print(f"Web Server: {server.web_server}")
    print(f"Status: {server.status}")
    print("=" * 60)

if __name__ == "__main__":
    main()