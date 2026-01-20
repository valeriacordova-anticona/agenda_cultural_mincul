# agenda_cultural_mincul

Agenda informativa del Ministerio de Cultura (Perú): Proyecto web informativo basado en la recopilación y análisis de titulares
publicados en la sección de noticias del Ministerio de Cultura del Perú (MINCUL).

Objetivo: Analizar la agenda informativa del Ministerio de Cultura mediante la extracción automatizada de titulares y URLs, y su posterior procesamiento para identificar patrones temáticos, frecuencia de palabras y extensión de los títulos periodísticos.

Fuente: https://www.gob.pe/institucion/cultura/noticias

Outputs:
data/raw_agenda.csv (Titulares y URLs de las noticias del MINCUL)
data/posts_python_blog_procesado.csv (Incluye los datos originales más la longitud del título)
data/top_palabras_titulos.csv (Ranking de las 20 palabras más frecuentes en los titulares)

Metodología:
Scraping HTML estático mediante requests y BeautifulSoup
Limpieza básica de texto
Análisis exploratorio de datos (EDA): Longitud de titulares, Frecuencia de palabras clave, Almacenamiento estructurado en CSV
Visualización web mediante GitHub Pages

Cómo ejecutar el proyecto:
pip install requests beautifulsoup4 pandas
python src/scrape.py
python src/process.py

Website: Los resultados se publican en un sitio web estático disponible a través de GitHub Pages, utilizando la carpeta /docs.
