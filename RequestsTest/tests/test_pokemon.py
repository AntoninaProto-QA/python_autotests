import requests
import pytest

host = 'https://pokemonbattle.me:9104/'

def test_status_code():
    response = requests.get(f'{host}trainers')

    assert response.status_code == 200

def test_my_trainer():
    response = requests.get(f'{host}trainers', params={"trainer_id" : 4014})
    assert response.json() ['trainer_name']== 'Proto_Tota'