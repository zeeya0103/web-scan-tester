import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.links = []

    def crawl(self, url=None):
        url = url or self.base_url
        if url in self.visited:
            return
        
        self.visited.add(url)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")
                if href:
                    full = urljoin(self.base_url, href)
                    if self.base_url in full:
                        self.links.append(full)
                        self.crawl(full)
        except Exception as e:
            print(f"Error crawling {url}: {e}")


# ✅ Updated to accept a URL argument
def run_crawler(base_url):
    c = Crawler(base_url)
    c.crawl()
    return c.links
