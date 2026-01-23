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


Prompt usado (IA)
Rol: Eres un ingeniero de datos y docente para comunicadores principiantes.
Contexto: Estoy en un curso de “Extracción y Procesamiento de Datos” (Python). Nunca he usado GitHub. Trabajamos con scraping estático y CSV. Queremos publicar resultados en un website con GitHub Pages usando la carpeta /docs.
Objetivo: Genera un proyecto con esta estructura: src/, data/, docs/. Crea 2 scripts en Python: (1) scraping de títulos+URLs de una página (requests+bs4) guardando CSV; (2) limpiar y tokenizar el texto, y procesamiento simple (longitud y top palabras) guardando 2 CSV (uno por cada objetivo). Luego crea docs/index.html que muestre links de descarga y una tabla leyendo los 3 CSV: raw_agenda , agenda_cultural_procesada y top_palabras. El URL que usaremos es https://www.gob.pe/institucion/cultura/noticias (Es la agenda de noticias del Ministerio de Cultura del Perú)
Restricciones: Código comentado, mensajes de éxito/errores claros, sin Selenium, compatible con Windows. Incluye instrucciones paso a paso y troubleshooting (qué revisar si el CSV sale vacío o el Pages no carga).
Output esperado: Pega el contenido completo de cada archivo: src/scrape.py, src/process.py, docs/index.html, README.md.
