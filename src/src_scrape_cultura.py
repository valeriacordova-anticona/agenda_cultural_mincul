# ============================================
# SCRAPING ESTÁTICO – NOTICIAS MINISTERIO DE CULTURA
# (versión filtrada y correcta)
# ============================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

URL = "https://www.gob.pe/institucion/cultura/noticias"

# -------------------------------
# 1. DESCARGAR HTML
# -------------------------------
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    print("✅ Página descargada correctamente")
except requests.RequestException as e:
    raise SystemExit(f"❌ Error al acceder a la página: {e}")

soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------
# 2. EXTRAER SOLO NOTICIAS
# -------------------------------
links = soup.find_all("a", href=True)

print(f"🔎 Enlaces totales encontrados: {len(links)}")

agenda = []
vistos = set()

for a in links:
    href = a["href"]
    titulo = a.get_text(strip=True)

    # --- FILTROS PERIODÍSTICOS ---
    if not titulo:
        continue

    if len(titulo) < 40:   # evita botones y menús
        continue

    if "/institucion/cultura/noticias/" not in href:
        continue

    if href in vistos:
        continue

    if href.startswith("/"):
        href = "https://www.gob.pe" + href

    vistos.add(href)

    agenda.append({
        "titulo": titulo,
        "url": href
    })

# -------------------------------
# 3. DATAFRAME
# -------------------------------
df = pd.DataFrame(agenda)

print("📰 Noticias válidas extraídas:", len(df))
print(df.head(5))

# -------------------------------
# 4. GUARDAR CSV
# -------------------------------
os.makedirs("data", exist_ok=True)
ruta = os.path.join("data", "raw_agenda.csv")

df.to_csv(ruta, index=False, encoding="utf-8")

print(f"✅ CSV guardado correctamente en: {ruta}")