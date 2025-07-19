import socket
import threading
import os
import time
import argparse

TEST_HOSTS = [
    "speedtest.serverius.net",
    "speed.hetzner.de",
    "speedtest-sgp1.digitalocean.com",
    "speedtest.ftp.otenet.gr",
    "www.speedtest.net",
    "fast.com",
    "www.speedcheck.ir",
    "www.testspeed.ir",
    "speedtest.amsterdam.linode.com",
]

def test_host_speed(host, port=80, test_size_mb=5):
    try:
        data = os.urandom(test_size_mb * 1024 * 1024)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        start = time.time()
        s.connect((host, port))
        s.sendall(b"POST /upload HTTP/1.1\r\nHost: " + host.encode() +
                  b"\r\nContent-Length: " + str(len(data)).encode() + b"\r\n\r\n")
        s.sendall(data)
        end = time.time()
        s.close()
        duration = end - start
        speed_mbps = (test_size_mb * 8) / duration  # in Mbps
        print(f"[+] Host {host} upload test: {speed_mbps:.2f} Mbps")
        return speed_mbps
    except Exception as e:
        print(f"[!] Host {host} failed: {e}")
        return 0

def find_best_host():
    print("[*] Testing hosts to find best upload speed...")
    best = max(TEST_HOSTS, key=lambda h: test_host_speed(h))
    print(f"[✅] Best upload host: {best}")
    return best

def upload_loop(host, port, size_mb, interval_sec):
    data = os.urandom(size_mb * 1024 * 1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.sendall(b"POST /upload HTTP/1.1\r\nHost: " + host.encode() +
                      b"\r\nContent-Length: " + str(len(data)).encode() + b"\r\n\r\n")
            s.sendall(data)
            s.close()
            print(f"[✓] Uploaded {size_mb} MB to {host}")
        except Exception as e:
            print(f"[!] Upload failed: {e}")
        time.sleep(interval_sec)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fake uploader tool")
    parser.add_argument("--host", help="Target host to upload (or leave empty to auto-detect)", default=None)
    parser.add_argument("--port", type=int, default=80, help="Port to use (default 80)")
    parser.add_argument("--size", type=int, default=50, help="Upload size in MB per loop")
    parser.add_argument("--interval", type=int, default=2, help="Seconds between uploads")
    args = parser.parse_args()

    target_host = args.host or find_best_host()
    upload_loop(target_host, args.port, args.size, args.interval)
