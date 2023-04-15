import requests
host = 'https://pokemonbattle.me:9104/'
token = '9d08557deee5f2cd5c910a868f92878c'
response = requests.post(f'{host}pokemons', headers = { "trainer_token": token, "Content-Type": "application/json"}, json={
    "name": "Тупатка",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
})
print(response.json()) #Запрос на создание покемона

response_change = requests.put(f'{host}pokemons', headers = { "trainer_token": token, "Content-Type": "application/json"}, json={
    "pokemon_id": "9245",
    "name": "Анатолий"
})
print(response_change.json()) #Запрос на изменение имени покемона

response_pokeball = requests.post(f'{host}trainers/add_pokeball', headers = { "trainer_token": token, "Content-Type": "application/json"}, json={
    "pokemon_id": "9246"
})
print(response_pokeball.json()) #Запрос на поимку покемона в покебол