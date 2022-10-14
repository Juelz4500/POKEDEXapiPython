import requests
import json

def search(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    response = requests.get(url)
    data = response.json()
    name = data["name"]
    abilities = data["abilities"][0]["ability"]["name"]
    base_experience = data["base_experience"]
    image = data["sprites"]["front_shiny"]
    attack = data["stats"][1]["base_stat"]
    hp = data["stats"][0]["base_stat"]
    defense = data["stats"][2]["base_stat"]
    
    print("Name: " + name)
    print("Abilities: " + abilities)
    print("Base Experience: " + base_experience)
    print("Image: " + image)
    print("Attack: " + attack)
    print("HP: " + hp)
    print("Defense: " + defense)
    
    search('bulbasaur')