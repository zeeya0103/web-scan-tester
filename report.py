doc = """
# WebScanPro – Documentation

## Overview
Automated tool to scan web applications for security vulnerabilities.

## Features
- Crawler
- SQL Injection Testing
- XSS Testing
- Session Testing
- IDOR Testing
- PDF Report Generation
"""

with open("DOCUMENTATION.md", "w") as f:
    f.write(doc)

print("[+] Documentation File Created!")
