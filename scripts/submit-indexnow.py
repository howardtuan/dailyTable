#!/usr/bin/env python3
"""Notify IndexNow after a successful deployment; receipt is not indexing."""

import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit


def main():
    root = Path(__file__).resolve().parents[1]
    host = (root / "CNAME").read_text().strip()
    key = (root / "indexnow-key.txt").read_text().strip()
    if not re.fullmatch(r"[a-zA-Z0-9-]{8,128}", key):
        raise ValueError("Invalid IndexNow key")
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text for node in ET.parse(root / "sitemap.xml").findall("s:url/s:loc", namespace)]
    if not urls or len(urls) > 10000 or len(set(urls)) != len(urls):
        raise ValueError("Sitemap must contain 1–10000 distinct page URLs")
    for url in urls:
        parsed = urlsplit(url)
        if parsed.scheme != "https" or parsed.netloc != host or parsed.query or parsed.fragment:
            raise ValueError("Unexpected sitemap URL: " + url)
    key_location = "https://" + host + "/indexnow-key.txt"
    live_key = subprocess.run(
        ["curl", "--fail", "--silent", "--show-error", "--max-time", "30", key_location],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    if live_key != key:
        raise ValueError("The deployed key does not match; wait for deployment before submitting")
    payload = {"host": host, "key": key, "keyLocation": key_location, "urlList": urls}
    with tempfile.TemporaryDirectory(prefix="dailytable-indexnow-") as directory:
        request = Path(directory) / "request.json"
        response = Path(directory) / "response.txt"
        request.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        status = subprocess.run(
            ["curl", "--silent", "--show-error", "--max-time", "30", "--request", "POST",
             "--header", "Content-Type: application/json; charset=utf-8", "--data-binary",
             "@" + str(request), "--output", str(response), "--write-out", "%{http_code}",
             "https://api.indexnow.org/indexnow"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        result = {"endpoint": "https://api.indexnow.org/indexnow", "httpStatus": int(status),
                  "urls": urls, "response": response.read_text()}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if status not in {"200", "202"}:
            return 1
        print("200 = received; 202 = received, key validation pending. Neither confirms indexing or ranking.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
