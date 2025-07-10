import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    # print(response)  # response returns the Http status code (200,404 ,...) 200 = OK , 404 = Page not found!

    if response.status_code == 200:
        pokemon_data = response.json()
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")