import os

footer_html = """<footer>
  Todos los conjuntos de datos bajo licencia CC0 1.0 · Acceso Abierto · juanmoisesdelaserna.es<br>
  <a href="https://juanmoisesdelaserna.es">juanmoisesdelaserna.es</a> ·
  <a href="https://orcid.org/0000-0002-8401-8018">ORCID</a> ·
  <a href="https://juanmoisesd.github.io/research-hub/">🌐 Hub Principal</a><br>
  <small style="color:#21262d">Actualizado: 2026-03-22</small>
</footer>"""

for root, dirs, files in os.walk('.'):
    if 'index.html' in files:
        path = os.path.join(root, 'index.html')
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        import re
        content = re.sub(r'<footer>.*?</footer>', footer_html, content, flags=re.DOTALL)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
