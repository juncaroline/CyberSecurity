Evitar pickle e outros formatos de serialização inseguros para dados vindos de usuários. Usar formatos seguros como JSON, YAML seguro, Protobuf, etc.

Se pickle for usado, nunca desserializar dados não confiáveis.

Validação e autenticação de entrada: aplicar assinatura digital no payload para garantir integridade.

Ambiente restrito (sandbox): Executar código em usuários com poucos privilégios e sem acesso a arquivos sensíveis.
