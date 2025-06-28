import re
import os
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def load_cookie_string(json_file):
    with open(json_file, 'r') as f:
        cookies = json.load(f)
    return "; ".join(f"{c['name']}={c['value']}" for c in cookies)

def extract_download_links(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    download_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        match = re.search(r"downloadMemories\('(.+?)'\)", href)
        if match:
            url = match.group(1)
            download_links.append(url)
    return download_links

def get_extension_from_url(url):
    if ".mp4" in url:
        return ".mp4"
    elif ".jpg" in url or ".jpeg" in url:
        return ".jpg"
    elif ".png" in url:
        return ".png"
    else:
        return ".bin"

def download_file(full_url, output_dir, count, cookie_string):
    parsed = urlparse(full_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    post_data = parsed.query

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://my.snapchat.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie_string
    }

    try:
        # Step 1: POST to get the AWS S3 link
        response = requests.post(base_url, data=post_data, headers=headers)
        if response.status_code == 200:
            s3_url = response.text.strip()
            if s3_url.startswith("http"):
                ext = get_extension_from_url(s3_url)
                filename = f"memory_{count:04d}{ext}"
                filepath = os.path.join(output_dir, filename)

                # Step 2: GET the actual media from the S3 URL
                media_response = requests.get(s3_url, stream=True)
                if media_response.status_code == 200:
                    with open(filepath, "wb") as f:
                        for chunk in media_response.iter_content(1024):
                            f.write(chunk)
                    print(f"[+] Downloaded: {filename}")
                else:
                    print(f"[-] Failed to fetch media from S3 (status {media_response.status_code})")
            else:
                print(f"[-] Unexpected response, not a URL: {s3_url[:100]}")
        else:
            print(f"[-] Failed (status {response.status_code}): {full_url}")
    except Exception as e:
        print(f"[!] Error downloading {full_url}: {e}")

def main():
    html_path = "memories_history.html"
    cookie_json = "www.snapchat.com_json_1751035506843.json"
    output_dir = "snapchat_memories"
    os.makedirs(output_dir, exist_ok=True)

    print("[*] Loading cookies...")
    cookie_string = load_cookie_string(cookie_json)

    print("[*] Extracting links from HTML...")
    links = extract_download_links(html_path)
    print(f"[*] Found {len(links)} memories.")

    for i, url in enumerate(links, start=1):
        download_file(url, output_dir, i, cookie_string)

if __name__ == "__main__":
    main()

