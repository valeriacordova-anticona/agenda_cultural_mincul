# ============================================
# PROCESAMIENTO DE TEXTO – AGENDA CULTURAL
# ============================================

import re
import pandas as pd
import os

# -------------------------------
# STOPWORDS (ES + EN)
# -------------------------------
STOPWORDS_ES = {
    "de","la","el","y","en","a","un","una","para","por","con",
    "del","los","las","al","ministerio","cultura","perú"
}

STOPWORDS_EN = {
    "the","and","to","of","in","for","on","with","a","an"
}

# -------------------------------
# FUNCIÓN DE TOKENIZACIÓN
# -------------------------------
def tokenizar(texto: str):
    """
    Limpia y tokeniza un texto:
    - pasa a minúsculas
    - elimina caracteres especiales
    - filtra stopwords
    - filtra tokens cortos
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ0-9\s-]", " ", texto)

    tokens = [t for t in texto.split() if len(t) >= 3]
    tokens = [
        t for t in tokens
        if t not in STOPWORDS_ES and t not in STOPWORDS_EN
    ]

    return tokens


# -------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------
def main():

    # ---------------------------
    # 1. CARGAR CSV ORIGINAL
    # ---------------------------
    ruta_entrada = os.path.join("data", "raw_agenda.csv")

    if not os.path.exists(ruta_entrada):
        raise SystemExit("❌ No existe data/raw_agenda.csv. Ejecuta primero scrape.py")

    df = pd.read_csv(ruta_entrada)

    print(f"📄 Noticias cargadas: {len(df)}")

    # ---------------------------
    # 2. PROCESAMIENTO BÁSICO
    #    (longitud del titular)
    # ---------------------------
    df["len_titulo"] = (
        df["titulo"]
        .fillna("")
        .astype(str)
        .str.len()
    )

    ruta_procesado = os.path.join("data", "agenda_cultura_procesada.csv")
    df.to_csv(ruta_procesado, index=False, encoding="utf-8")

    print(f"✅ Archivo generado: {ruta_procesado}")

    # ---------------------------
    # 3. TOP PALABRAS (AGENDA)
    # ---------------------------
    all_tokens = []

    for t in df["titulo"].fillna("").astype(str):
        all_tokens.extend(tokenizar(t))

    freq = (
        pd.Series(all_tokens)
        .value_counts()
        .head(20)
        .reset_index()
        .rename(columns={
            "index": "palabra",
            0: "conteo"
        })
    )

    ruta_top = os.path.join("data", "top_palabras_titulos.csv")
    freq.to_csv(ruta_top, index=False, encoding="utf-8")

    print(f"✅ Archivo generado: {ruta_top}")


# -------------------------------
# EJECUCIÓN
# -------------------------------
if __name__ == "__main__":
    main()