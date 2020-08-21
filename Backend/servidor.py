from config import *
from modelo import Idioma

@app.route("/")
def inicio():
	return "Sistema de registro informacional de idiomas. "+\
		"<a href='/listar_info_idiomas'>Listar informações dos idiomas</a>"

@app.route("/listar_info_idiomas")
def listar_info_idiomas():
	
	idiomas = db.session.query(Idioma).all()
	
	idiomas_em_json = [i.json() for i in idiomas]

	print(idiomas_em_json)

	resposta = jsonify(idiomas_em_json)

	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

# Macintosh - Linux -> curl -d '{"dificuldade":"prakct", "id":1, "nome":"sufubaru", "popularidade":"nossademaisdaconta"}' -X POST -H "Content-Type: application/json" localhost:5000/incluir_info_idioma
# Windirs riririri -> curl --data "{\"id\": 25, \"nome\": \"sufubaru\", \"dificuldade\": \"prakct\", \"popularidade\": \"nossademaisdaconta\"}" -X POST -H "Content-Type: application/json" localhost:5000/incluir_info_idioma
@app.route("/incluir_info_idioma", methods=['POST'])
def incluir_info_idioma():

	resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

	dados = request.get_json()

	try:

		idioma = Idioma(**dados)

		# debug
		#print("[Adicionando objeto] : ", type(idioma))

		db.session.add(idioma)
		db.session.commit()

	except Exception as e:

		resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
	
	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/excluir_info_idioma", methods=['GET'])
def excluir_info_idioma():

	resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

	try:
		
		id = int(request.args.get("id"))

		if (id < 1):

			resposta = jsonify({"resultado":"erro", "detalhes":"O id necessita ser maior ou igual a 1."})

		else:
			
			idioma = db.session.query(Idioma).get(id)
			
			# debug
			#print("[Excluindo objeto] : ", idioma)

			if (idioma is not None):

				db.session.delete(idioma)
				db.session.commit()

			else:

				resposta = jsonify({"resultado":"erro", "detalhes":"Informação sobre idioma não encontrada."})

	except Exception as e:

		resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

@app.route("/alterar_info_idioma", methods=['GET', 'POST'])
def alterar_info_idioma():

	resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

	if request.method == 'GET':

		try:
		
			id = int(request.args.get("id"))

			if (id < 1):

				resposta = jsonify({"resultado":"erro", "detalhes":"O id necessita ser maior ou igual a 1."})

			else:

				if (db.session.query(Idioma).get(id) is None):

					resposta = jsonify({"resultado":"erro", "detalhes":"Informação sobre idioma não encontrada."})

		except Exception as e:

			resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

	else:

		try:

			dados = request.get_json()
			idioma = Idioma(**dados)

			db.session.query(Idioma).filter(Idioma.id == idioma.id).update(dados)
			db.session.commit()

		except Exception as e:

			resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

	resposta.headers.add("Access-Control-Allow-Origin", "*")

	return resposta

if __name__ == "__main__":

	app.run(debug=True)