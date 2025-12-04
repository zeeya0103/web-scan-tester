import requests

class AuthTester:
    def __init__(self, login_url):
        self.url = login_url

    def brute_force(self):
        usernames = ["admin", "test"]
        passwords = ["password", "1234", "admin"]

        for u in usernames:
            for p in passwords:
                data = {"username": u, "password": p}
                r = requests.post(self.url, data=data)
                if "Welcome" in r.text:
                    print("[+] Weak Credentials Found:", u, p)
                    return

    def session_test(self):
        s = requests.Session()
        r = s.get(self.url)
        print("[*] Session Cookie:", s.cookies)

# FIXED: use localhost, not dvwa
auth = AuthTester("http://localhost/login.php")
auth.brute_force()
auth.session_test()
