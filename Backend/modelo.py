from config import *

linguas_do_pais = db.Table('linguas_do_pais',
	db.Column('pais_id', db.Integer, db.ForeignKey('pais.pais_id')),
	db.Column('idioma_id', db.Integer, db.ForeignKey('idioma.idioma_id'))
)

class Pais(db.Model):

	pais_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(254))
	linguas_do_pais = db.relationship('Idioma', secondary=linguas_do_pais, backref=db.backref('linguas_do_pais', lazy = 'dynamic'))

	def __str__(self):

		desc_idiomas = ""
		linguas = []

		for contador, idioma in enumerate(self.linguas_do_pais):
			linguas.append(idioma.nome)
			desc_idiomas += f"\n\t[{contador}] {str(idioma)}\n"

		return f"Pais [{self.pais_id}] cujo nome é {self.nome}, no qual vigora a(s) língua(s) {linguas}\
			\n{desc_idiomas}\n"

		"""
		return str(self.id)+") " + self.nome + ", " + \
			str(self.idioma_id) + ", " + str(self.idioma)
		"""

	def json(self):

		return {

			"pais_id": self.pais_id,
			"nome": self.nome,
			"linguas_do_pais": [idioma.json() for idioma in self.linguas_do_pais]

		}

		"""

		return {

			"id": self.id,
			"nome": self.nome,
			"idioma_id": self.idioma_id,
			"idioma": self.idioma.json()

		}

		"""


class Idioma(db.Model):

	idioma_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(254))
	dificuldade = db.Column(db.String(254))
	popularidade = db.Column(db.String(254))

	def __str__(self):

		return f"{self.nome} é considerado {self.dificuldade.lower()} de aprender e é {self.popularidade.lower()} ao redor do mundo"

		"""
		return str(self.id)+") "+ self.nome + ", " +\
			str(self.dificuldade) + ", " + str(self.popularidade)
		"""

	def json(self):

		return {
			"idioma_id": self.idioma_id,
			"nome": self.nome,
			"dificuldade": self.dificuldade,
			"popularidade": self.popularidade
		}


if __name__ == "__main__":
	
	if exists(arquivobd):
		rmfile(arquivobd)

	db.create_all()
	
	tads_unids = Pais(nome = "Estados Unidos")
	japao = Pais(nome = "Japão")
	alemanha = Pais(nome = "Alemanha")
	russia = Pais(nome = "Russia")
	china = Pais(nome = "China")

	db.session.add(tads_unids)
	db.session.add(japao)
	db.session.add(alemanha)
	db.session.add(russia)
	db.session.add(china)

	ingles = Idioma(nome = "Inglês", dificuldade = "Fácil", 
		popularidade = "Extremamente popular")

	japones = Idioma(nome = "Japonês", dificuldade = "Difícil",
		popularidade = "Popular")

	alemao = Idioma(nome = "Alemão", dificuldade = "Difícil",
		popularidade = "Popular")

	russo = Idioma(nome = "Russo", dificuldade = "Difícil",
		popularidade = "Popular")

	mandarim = Idioma(nome = "Mandarim", dificuldade = "Extremamente difícil",
		popularidade = "Muito popular")

	db.session.add(ingles)
	db.session.add(japones)
	db.session.add(alemao)
	db.session.add(russo)
	db.session.add(mandarim)

	tads_unids.linguas_do_pais.append(ingles)

	japao.linguas_do_pais.append(japones)

	alemanha.linguas_do_pais.append(alemao)
	alemanha.linguas_do_pais.append(ingles)

	russia.linguas_do_pais.append(russo)

	china.linguas_do_pais.append(mandarim)

	db.session.commit()

	for pais in db.session.query(Pais):
		print(pais.json(), end="\n\n")

	db.session.query(Idioma).filter(Idioma.idioma_id == ingles.idioma_id)

	#for lingua in pais.linguas_do_pais:
	#	print(str(lingua))

	#db.session.query(User.name).filter(User.id == 1).first()
	#idioma = db.session.query(Idioma).filter(Idioma.id == id)
	
	"""

	idioma = db.session.query(Idioma).get(6)
	print(idioma)

	print(db.session.delete(idioma))
	idioma = db.session.query(Idioma).get(6)
	print("antes do commit: ", idioma)
	db.session.commit()

	idioma = db.session.query(Idioma).get(6)
	print(idioma)


	paises = db.session.query(Pais)
	for pais in paises:
		print(pais)
	"""

	#print(idioma5)
	#print(idioma5.json())