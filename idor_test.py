import requests

class IDORTester:

    def __init__(self, base_url):
        # DVWA IDOR path
        self.url = f"{base_url}/vulnerabilities/idor/"

    def test_idor(self):
        results = []

        # DVWA has users 1–5 by default
        for user_id in range(1, 10):
            try:
                r = requests.get(self.url, params={"id": user_id})

                response_text = r.text.lower()

                # DVWA IDOR indicators
                idor_indicators = [
                    "first name",
                    "surname",
                    "user id",
                    "username",
                    "member"
                ]

                if any(indicator in response_text for indicator in idor_indicators):
                    results.append({
                        "type": "IDOR",
                        "url": self.url,
                        "user_id": user_id,
                        "severity": "High",
                        "evidence": f"User data visible for id={user_id}"
                    })

            except Exception:
                continue

        return results
