import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

URL_FILE = "data/urls.txt"
OUTPUT_FILE = "data/scraped_data.txt"


def scrape_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            print(f"Failed: {url}")
            return ""

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = []

        for p in paragraphs:
            line = p.get_text(" ", strip=True)

            if line:
                text.append(line)

        return "\n".join(text)

    except Exception as e:
        print(e)
        return ""


def main():
    with open(URL_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        for url in urls:
            print("Scraping:", url)

            data = scrape_page(url)

            out.write("=" * 80 + "\n")
            out.write(url + "\n")
            out.write("=" * 80 + "\n")
            out.write(data + "\n\n")

            time.sleep(2)

    print("Finished.")


if __name__ == "__main__":
    main()