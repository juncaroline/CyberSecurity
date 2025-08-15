Tipo de vulnerabilidade: SSRF (Server-side request forgery) + LFI (Local File Inclusion)

SSRF é uma vulnerabilidade que permite que o hacker envie requisições do backend do software para outro servidor ou para um serviço local. O servidor ou serviço que recebe tal requisição acredita que veio de uma aplicação confiável. Essa vulnerabilidade pode ser inserida quando é usado o input do usuário para criar uma requisição, como por exemplo, criando uma URL.

LFI é uma vulnerabilidade web que permite o hacker acessar, visualizar e/ou incluir arquivos encontrados no sistema de arquivos do servidor web dentro da pasta raiz do documento. Acontece quando uma aplicação permite que o usuário informe o caminho de um arquivo local para ser carregado ou incluído sem validação adequada.