class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou ataque desconhecido'

        mensagem = f"O {self.tipo} atacou usando {ataque}"
        print(mensagem)

heroi1 = Heroi(nome="Herói 1", idade=25, tipo="mago")
heroi2 = Heroi(nome="Herói 2", idade=30, tipo="guerreiro")
heroi3 = Heroi(nome="Herói 3", idade=22, tipo="monge")

heroi1.atacar()  
heroi2.atacar()
heroi3.atacar()