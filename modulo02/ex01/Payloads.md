serializer.py
return (str, ("cat /etc/passwd",))
return (str, ("ls -la",))
return (str, ("echo 'Hacked!' > /tmp/test.txt",))

poderia ser usado para acessar outros dados do sistema, criar arquivos dentro do sistema, etc.

Onde essa vulnerabilidade pode ser explorada:
- Aplicações web com sessões serializadas no cliente
- APIs que recebem objetos serializados