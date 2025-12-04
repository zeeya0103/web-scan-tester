import requests

class XSSTester:

    def __init__(self, base_url):
        # DVWA reflected XSS page
        self.url = f"{base_url}/vulnerabilities/xss_r/"

    def test_xss(self):
        results = []

        payloads = [
            "<script>alert(1)</script>",
            "\"><script>alert(1)</script>"
        ]

        for payload in payloads:
            try:
                # DVWA reflected XSS uses the 'name' GET parameter
                r = requests.get(self.url, params={"name": payload})

                # Check if payload reflects back (indicating vulnerability)
                if payload in r.text:
                    results.append({
                        "type": "XSS",
                        "url": self.url,
                        "payload": payload,
                        "severity": "Medium",
                        "evidence": "Payload reflected in HTML response"
                    })

            except Exception:
                continue

        return results
