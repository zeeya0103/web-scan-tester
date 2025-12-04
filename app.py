import time
import requests
from auth_test import AuthTester
from crawler import run_crawler
from idor_test import IDORTester
from sqli_test import SQLInjectionTester
from xss_test import XSSTester

DVWA_URL = "http://localhost/login.php"


# Check DVWA status
def wait_for_dvwa():
    print("[*] Waiting for DVWA to be ready...")
    for i in range(20):
        try:
            r = requests.get(DVWA_URL, timeout=5)
            if r.status_code == 200:
                print("[+] DVWA is ready!")
                return True
        except requests.exceptions.RequestException:
            print(f"[!] Not ready, retrying ({i+1}/20)...")
            time.sleep(3)
    print("[X] DVWA did not respond. Exiting.")
    return False


if __name__ == "__main__":

    if not wait_for_dvwa():
        exit(1)

    print("[+] Starting WebScanPro...\n")

    try:
        print("[*] Running Auth Tester...")
        auth = AuthTester(DVWA_URL)
        auth.brute_force()
        print("[✓] Auth Test Completed.\n")
    except Exception as e:
        print("[ERROR] Auth Test Failed:", e)

    try:
        print("[*] Running Crawler...")
        run_crawler(DVWA_URL)
        print("[✓] Crawling Completed.\n")
    except Exception as e:
        print("[ERROR] Crawler Failed:", e)

    try:
        print("[*] Running IDOR Test...")
        IDORTester(DVWA_URL).test_idor()
        print("[✓] IDOR Test Completed.\n")
    except Exception as e:
        print("[ERROR] IDOR Test Failed:", e)

    try:
        print("[*] Running SQL Injection Test...")
        SQLInjectionTester(DVWA_URL).test_sql()
        print("[✓] SQL Injection Test Completed.\n")
    except Exception as e:
        print("[ERROR] SQLi Test Failed:", e)

    try:
        print("[*] Running XSS Test...")
        XSSTester(DVWA_URL).test_xss()
        print("[✓] XSS Test Completed.\n")
    except Exception as e:
        print("[ERROR] XSS Test Failed:", e)

    print("\n[+] WebScanPro Finished!\n")
