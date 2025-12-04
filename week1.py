import requests

class WebScanPro:
    def __init__(self, base_url):
        self.base_url = base_url
        print("[+] Project Initialized!")

    def check_connection(self):
        try:
            r = requests.get(self.base_url)
            if r.status_code == 200:
                print("[+] Connection Successful!")
            else:
                print("[-] Error:", r.status_code)
        except:
            print("[-] Cannot reach target!")

scanner = WebScanPro("http://localhost")
scanner.check_connection()
