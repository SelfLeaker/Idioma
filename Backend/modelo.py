from config import *

class Idioma(db.Model):

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(254))
	dificuldade = db.Column(db.String(254))
	popularidade = db.Column(db.String(254))

	def __str__(self):
		return str(self.id)+") "+ self.nome + ", " +\
			str(self.dificuldade) + ", " + str(self.popularidade)

	def json(self):
		return {
			"id": self.id,
			"nome": self.nome,
			"dificuldade": self.dificuldade,
			"popularidade": self.popularidade
		}

if __name__ == "__main__":
	
	if exists(arquivobd):
		rmfile(arquivobd)

	db.create_all()

	idioma1 = Idioma(nome = "Inglês", dificuldade = "Fácil", 
		popularidade = "Extremamente popular")

	idioma2 = Idioma(nome = "Japonês", dificuldade = "Difícil",
		popularidade = "Popular")

	idioma3 = Idioma(nome = "Alemão", dificuldade = "Difícil",
		popularidade = "Popular")

	idioma4 = Idioma(nome = "Russo", dificuldade = "Difícil",
		popularidade = "Popular")

	idioma5 = Idioma(nome = "Mandarim", dificuldade = "Extremamente difícil",
		popularidade = "Muito popular")
	
	idioma6 = Idioma(nome = "dummy", dificuldade = "Extremamente difícil",
		popularidade = "Muito popular")

	db.session.add(idioma1)
	db.session.add(idioma2)
	db.session.add(idioma3)
	db.session.add(idioma4)
	db.session.add(idioma5)
	db.session.add(idioma6)
	db.session.commit()
	
	#db.session.query(User.name).filter(User.id == 1).first()
	#idioma = db.session.query(Idioma).filter(Idioma.id == id)
	idioma = db.session.query(Idioma).get(6)
	print(idioma)

	print(db.session.delete(idioma))
	idioma = db.session.query(Idioma).get(6)
	print("antes do commit: ", idioma)
	db.session.commit()

	idioma = db.session.query(Idioma).get(6)
	print(idioma)

	#print(idioma5)
	#print(idioma5.json())