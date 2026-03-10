import urllib.request
import gzip

url = "https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz"

# télécharger le fichier
urllib.request.urlretrieve(url, "epg.xml.gz")

# décompresser
with gzip.open("epg.xml.gz", "rb") as f:
    data = f.read().decode("utf-8", errors="ignore")

# modifier les noms de chaines
data = data.replace("CAF ", "CA FR ")
data = data.replace("CA-BK", "CA EN")
data = data.replace("CA BK", "CA EN")

# sauvegarder
with open("epg_ca.xml", "w", encoding="utf-8") as f:
    f.write(data)

print("EPG généré")
