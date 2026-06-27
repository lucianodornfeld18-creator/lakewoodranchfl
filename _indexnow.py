#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex, etc.) with every URL in sitemap.xml.
Run AFTER the domain is live at https://lakewoodranchconcretefl.com
(IndexNow validates the key file at the domain root first).

Usage:  py _indexnow.py
"""
import os, re, json, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
KEY = "f5df87f67fa441bb9dee77b7f914f1a8"
HOST = "lakewoodranchconcretefl.com"

sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
urls = re.findall(r"<loc>([^<]+)</loc>", sm)
print(f"Submitting {len(urls)} URLs to IndexNow…")

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": f"https://{HOST}/{KEY}.txt",
    "urlList": urls,           # IndexNow allows up to 10,000 per request
}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
try:
    with urllib.request.urlopen(req) as r:
        print("HTTP", r.status, "— OK, URLs submitted." if r.status == 200 else r.read())
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.reason)
    print("Note: 403 = key file not reachable yet (domain not live?); 422 = host/key mismatch.")
