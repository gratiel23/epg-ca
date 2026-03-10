import gzip
import requests

url = "https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz"

# télécharger le fichier
r = requests.get(url, timeout=60)
with open("epg.xml.gz", "wb") as f:
    f.write(r.content)

# décompresser correctement
with gzip.open("epg.xml.gz", "rb") as f:
    data = f.read().decode("utf-8", errors="ignore")

# remplacer les noms
data = data.replace("CAF ", "CA FR ")
data = data.replace("CA-BK", "CA EN")
data = data.replace("CA BK", "CA EN")

# sauvegarder le nouveau EPG
with open("epg_ca.xml", "w", encoding="utf-8") as f:
    f.write(data)

print("EPG généré")
