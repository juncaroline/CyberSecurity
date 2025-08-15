SSRF:
	- Não confiar em dados do usuário quando acessar outros servidores.
	- Validar e filtrar URLs confiáveis
	- Whitelist os hostnames ou endereços de IP que a sua aplicação precisa acessar. Permitir apenas domínios ou protocolos específicos (confiáveis)
	- Timeout e limite de redirecionamento
	- Isolamento de rede, ou seja, servidores que fazem requisições não devem ter acesso à rede interna

LFI:
	- Nunca usar inputs de usuário para carregar arquivos
	- Usar whitelist de arquivos os IDs (e não caminhos)
	- Não incluir arquivos dinamicamente
	- Sanitizar input (não aceitar inputs com ../, %2e%2e/)