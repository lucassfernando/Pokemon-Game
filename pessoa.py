from pokemon import *



class Pessoa:

    def __init__(self, nome=None, pokemons=[]):

        if nome:
            self.nome = nome
        else:
            self.nome = 'Anonimo'
        
        self.pokemons = pokemons
    
    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):

        if self.pokemons:
            
            print(f"Pokemons de {self}:")

            for pokemon in self.pokemons:
            
                print(pokemon)
           
        else:
            
            print("você não tem pokemons")

class Player(Pessoa):

    tipo = 'player'

    def capturar(self, pokemon):

        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}")

class Inimigo(Pessoa):

    tipo = 'inimigo'

pokemon_1 = PokemonEletrico('pikachu')

eu = Player('Lucas', [pokemon_1])

pokemon_selvagem = PokemonFogo('charmander')

eu.mostrar_pokemons()



