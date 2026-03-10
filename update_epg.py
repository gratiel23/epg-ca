import requests
import gzip

url = "https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*"
}

r = requests.get(url, headers=headers, timeout=60)

with open("epg.xml.gz", "wb") as f:
    f.write(r.content)

with gzip.open("epg.xml.gz", "rb") as f:
    xml = f.read().decode("utf-8", errors="ignore")

xml = xml.replace("CAF ", "CA FR ")
xml = xml.replace("CA-BK", "CA EN")
xml = xml.replace("CA BK", "CA EN")

with open("epg_ca.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("EPG generated")
