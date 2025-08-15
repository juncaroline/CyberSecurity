- Nunca renderizar diretamente do input do usuário, como por exemplo:
	return render_template("template.html", msg=request.args.get("msg"))
	e sim
	user_input = request.args.get("msg")
	return render_template("template.html", msg=escape(user_input))
- Fazer validação e sanitização dos dados de entrada (tipo, tamanho, formato, lista de valores permitidos)
- Usar ambientes restritos (sandbox)