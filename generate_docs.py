from jinja2 import Environment, FileSystemLoader

# ---------------------------------------------------------
# Vulnerabilities (sample data) — replace with your results
# ---------------------------------------------------------
vulnerabilities = [
    {
        "type": "SQL Injection",
        "file": "login.php",
        "severity": "High",
        "evidence": "Input vulnerable to SQL payload ' OR '1'='1",
        "mitigation": "Use prepared statements and strict input validation."
    },
    {
        "type": "Broken Authentication",
        "file": "admin.php",
        "severity": "High",
        "evidence": "Weak login protection allows brute-force attacks",
        "mitigation": "Enable rate limiting & secure password policy."
    },
    {
        "type": "Reflected XSS",
        "file": "profile.php",
        "severity": "Medium",
        "evidence": "<script>alert(1)</script> reflection detected",
        "mitigation": "Sanitize user input & use CSP."
    },
    {
        "type": "Directory Listing Enabled",
        "file": "/uploads/",
        "severity": "Low",
        "evidence": "Directory contents visible",
        "mitigation": "Disable directory listing in server config."
    },
    {
        "type": "Unidentified Pattern",
        "file": "unknown",
        "severity": "Unclassified",
        "evidence": "Scanner unable to determine severity",
        "mitigation": "Manual review required."
    }
]

# ---------------------------------------------------------
# Count severity for chart
# ---------------------------------------------------------
severity_count = {"High": 0, "Medium": 0, "Low": 0, "Unclassified": 0}

for v in vulnerabilities:
    sev = v["severity"]
    if sev in severity_count:
        severity_count[sev] += 1
    else:
        severity_count["Unclassified"] += 1

# ---------------------------------------------------------
# Auto-generate Findings Summary
# ---------------------------------------------------------
findings_parts = []

if severity_count["High"] > 0:
    findings_parts.append(
        f"{severity_count['High']} high-severity vulnerabilities detected. "
        "These pose critical risks and require immediate attention."
    )

if severity_count["Medium"] > 0:
    findings_parts.append(
        f"{severity_count['Medium']} medium-severity issues found. "
        "These can impact security if combined with other weaknesses."
    )

if severity_count["Low"] > 0:
    findings_parts.append(
        f"{severity_count['Low']} low-severity issues found. "
        "These are minor but should be fixed for better security hygiene."
    )

if severity_count["Unclassified"] > 0:
    findings_parts.append(
        f"{severity_count['Unclassified']} findings could not be classified. "
        "These require manual inspection."
    )

findings_text = " ".join(findings_parts)

# ---------------------------------------------------------
# Render HTML
# ---------------------------------------------------------
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("report_template.html")

html_output = template.render(
    vulnerabilities=vulnerabilities,
    severity_labels=list(severity_count.keys()),
    severity_values=list(severity_count.values()),
    findings=findings_text
)

with open("security_report.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✔ Report generated successfully: security_report.html")