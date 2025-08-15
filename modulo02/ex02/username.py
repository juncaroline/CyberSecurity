import re
from urllib.parse import urljoin
from urllib.request import urlopen

base_url = "http://localhost:8085/"

def get_content(url):
    try:
        with urlopen(url) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"[!] Erro ao baixar {url}: {e}")
        return ""

# Baixa a página inicial
html = get_content(base_url)

# Procura links para arquivos .js no HTML
js_files = re.findall(r'src=["\'](.*?\.js)["\']', html)

# Lista de arquivos a inspecionar (HTML + JS encontrados)
files_to_check = [(base_url, html)]

for js in js_files:
    js_url = urljoin(base_url, js)
    js_content = get_content(js_url)
    if js_content:
        files_to_check.append((js_url, js_content))

# Padrões comuns de credenciais
patterns = [
    r"(?:user|username|login)\s*[:=]\s*[\"']([^\"']+)[\"']",
    r"(?:pass|password)\s*[:=]\s*[\"']([^\"']+)[\"']"
]

print("\n=== Possíveis credenciais encontradas ===")
for url, content in files_to_check:
    for pat in patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        for m in matches:
            print(f"[{url}] → {m}")

