import urllib.request
import gzip

url = "https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz"

req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

with urllib.request.urlopen(req) as response:
    data = response.read()

with open("epg.xml.gz", "wb") as f:
    f.write(data)

with gzip.open("epg.xml.gz", "rb") as f:
    xml = f.read().decode("utf-8", errors="ignore")

xml = xml.replace("CAF ", "CA FR ")
xml = xml.replace("CA-BK", "CA EN")
xml = xml.replace("CA BK", "CA EN")

with open("epg_ca.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("EPG generated")
