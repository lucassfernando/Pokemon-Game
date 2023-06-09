import random


class Pokemon:
    
    def __init__(self, especie, level=None ,nome=None):

        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie
            
    def __str__(self):

        return f"{self.nome} ({self.level})"
        
    def atacar(self, inimigo_pokemon):

        print(f"{self.especie} atacou {inimigo_pokemon.especie}")

class PokemonFogo(Pokemon):

    tipo = 'fogo'

    def atacar(self, inimigo_pokemon):

        print(f"{self} lançou chamas em {inimigo_pokemon}")

class PokemonEletrico(Pokemon):

    tipo = 'eletrico'

    def atacar(self, inimigo_pokemon):

        print(f"{self} lançou raio em {inimigo_pokemon}")

class PokemonAgua(Pokemon):

    tipo = 'agua'

    def atacar(self, inimigo_pokemon):

        print(f"{self} lançou agua em {inimigo_pokemon}")





