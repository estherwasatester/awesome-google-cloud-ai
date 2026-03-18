import csv
import urllib.request
from urllib.error import HTTPError, URLError
import socket
import os

def check_url(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=3)
        return True
    except Exception as e:
        return False

mcps = set()
exts = set()
skills = set()

csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'maad_stack.csv')
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        mcp = row.get('MCP Server (GitHub)', '').strip()
        if mcp:
            for m in mcp.split(','):
                mcps.add(m.strip())
                
        ext = row.get('Gemini CLI Extension', '').strip()
        if ext:
            for e in ext.split(','):
                exts.add(e.strip())
                
        skill = row.get('Agent Skills', '').strip()
        if skill:
            for s in skill.split(','):
                if s.strip():
                    skills.add(s.strip())

print("Checking MCPs:")
for url in sorted(mcps):
    res = 'OK' if check_url(url) else 'FAIL'
    print(f"[{res}] {url}")

print("\nChecking Extensions:")
for url in sorted(exts):
    res = 'OK' if check_url(url) else 'FAIL'
    print(f"[{res}] {url}")

print("\nChecking Skills:")
for url in sorted(skills):
    res = 'OK' if check_url(url) else 'FAIL'
    print(f"[{res}] {url}")
