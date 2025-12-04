import time
import requests
import subprocess

DVWA_URL = "http://dvwa/login.php"

print("[*] Waiting for DVWA to be ready...")
for i in range(20):  # retry 20 times (100 seconds)
    try:
        r = requests.get(DVWA_URL)
        if r.status_code == 200:
            print("[+] DVWA is ready!")
            break
    except requests.exceptions.ConnectionError:
        print("[!] DVWA not ready, waiting 5 seconds...")
        time.sleep(5)
else:
    print("[X] DVWA did not start. Exiting.")
    exit(1)

# Run WebScanPro main script
print("[*] Starting WebScanPro...")
subprocess.run(["python", "app.py"])
