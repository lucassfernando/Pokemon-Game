import random

from pokemon import *


lista_nomes = ['Luan', 'Jorge', 'Carlos', 'Maria', 'Julia', 'Fernanda']
lista_pokemons = [PokemonAgua('Squirtle'),
                  PokemonEletrico('Pikachu'),
                  PokemonFogo('Charmander')]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(lista_nomes)
        
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

    def __init__(self, nome=None, pokemons=[]):

        if not pokemons:
            
            for pokemons_sorteados in range(random.randint(1, 2)):
                
                pokemons.append(random.choice(lista_pokemons))
        
        super().__init__(nome=nome, pokemons=pokemons)

meu_inimigo = Inimigo()

print(meu_inimigo)
meu_inimigo.mostrar_pokemons()

meu_pok = PokemonFogo('charmander')








