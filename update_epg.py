import gzip
import requests

url = "https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz"

r = requests.get(url, timeout=60)
open("epg.xml.gz","wb").write(r.content)

with gzip.open("epg.xml.gz","rt",encoding="utf8") as f:
    data = f.read()

data = data.replace("CAF ", "CA FR ")
data = data.replace("CA-BK", "CA EN")
data = data.replace("CA BK", "CA EN")

with open("epg_ca.xml","w",encoding="utf8") as f:
    f.write(data)
