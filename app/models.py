class Aluno:
    def __init__(self, nome, idade, github, linkedin, serie, cpf, uf, cidade, mini_bio, foto):
        self.nome = nome
        self.idade = idade
        self.github = github
        self.linkedin = linkedin
        self.serie = serie
        self.cpf = cpf
        self.uf = uf
        self.cidade = cidade
        self.mini_bio = mini_bio
        self.foto = foto

class Professor:
    def __init__(self, nome, idade, telefone, email, github, linkedin, bio, foto):
        self.nome = nome
        self.idade= idade
        self.telefone = telefone
        self.email = email
        self.github = github
        self.linkedin = linkedin
        self.bio = bio
        self.foto = foto
