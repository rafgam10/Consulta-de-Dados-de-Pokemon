import requests
import json

def requisicaoHTTPDoPokemon(nomeOuIdPokemon):
    requisicao = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nomeOuIdPokemon}")
    return requisicao




