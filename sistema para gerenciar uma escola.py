class SalaDeAula:
    def __init__(self, numero, capacidade, andar):
        self.numero = numero
        self.capacidade = capacidade
        self.andar = andar
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Sala {self.numero} reservada.")
        else:
            print(f"Sala {self.numero} já está ocupada.")

    def liberar(self):
        self.ocupada = False
        print(f"Sala {self.numero} liberada.")


class Professor:
    def __init__(self, nome, matricula, disciplina):
        self.nome = nome
        self.matricula = matricula
        self.disciplina = disciplina
        self.escolas = []

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)
            print(f"{self.nome} foi associado à escola {escola.nome}.")


class Endereco:
    def __init__(self, logradouro, numero, cidade, cep):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.cep = cep

    def exibir_endereco(self):
        print(
            f"{self.logradouro}, {self.numero} - "
            f"{self.cidade} - CEP: {self.cep}"
        )

    def atualizar_endereco(self, logradouro, numero, cidade, cep):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.cep = cep


class Aluno:
    def __init__(self, nome, matricula, data_nascimento, endereco):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento

        # Agregação
        # O endereço é recebido de fora da classe.
        self.endereco = endereco

    def matricular(self):
        print(f"Aluno {self.nome} matriculado.")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Nascimento: {self.data_nascimento}")
        self.endereco.exibir_endereco()


class Escola:
    def __init__(self, nome, cnpj, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone

        # Composição
        # A escola cria e controla suas próprias salas.
        self.salas = []

        # Associação
        self.professores = []

    def adicionar_sala(self, numero, capacidade, andar):
        sala = SalaDeAula(numero, capacidade, andar)
        self.salas.append(sala)

        print(f"Sala {numero} adicionada à escola {self.nome}.")

    def remover_sala(self, numero):
        self.salas = [
            sala for sala in self.salas
            if sala.numero != numero
        ]

        print(f"Sala {numero} removida da escola.")

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)

            if self not in professor.escolas:
                professor.escolas.append(self)

            print(
                f"Professor {professor.nome} associado "
                f"à escola {self.nome}."
            )
