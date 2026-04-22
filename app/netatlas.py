import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import IPv4Network


def ping(ip):
    system = platform.system().lower()
    param = "-n" if system == "windows" else "-c"
    timeout_param = "-w" if system == "windows" else "-W"
    command = ["ping", param, "1", timeout_param, "1", str(ip)]

    try:
        result = subprocess.run(
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=2
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, Exception):
        return False


def scan_network(cidr):
    network = IPv4Network(cidr, strict=False)
    active_hosts = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_ip = {executor.submit(ping, ip): ip for ip in network.hosts()}

        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                if future.result():
                    print(f"[+] Host alive: {ip}")
                    active_hosts.append(str(ip))
            except Exception:
                pass

    return active_hosts


if __name__ == "__main__":
    scan_network("192.168.1.0/24")
