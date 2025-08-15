file:///etc/passwd
	saída esperada conforme subject

file:///proc/self/environ
	retorna a variável de ambiente PATH


Onde essa vulnerabilidade pode ser explorada:
SSRF:
	- Quando a aplicação permite entradas de URLs
	- Quando o servidor tenta acessar recursos internos
	- Quando bibliotecas como request.get() são usadas diretamente com o input do usuário

LFI:
	- Quando a aplicação carrega arquivos locais com base em parâmetros (ex: ?file=...)
	- Quando nome de templates, imagens ou outras inclusões são definidas pelo usuário sem validação
	- Quando diretórios estão mal protegidos ou tem listagem ativada