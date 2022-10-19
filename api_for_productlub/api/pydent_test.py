import requests

from pydantic import BaseModel, ValidationError

url = 'https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json'
response = requests.get(url)
obj = response.json()
#print(obj)

#obj = str(response.json()).replace("\'", "\"")


class Card(BaseModel):
    id: int
    brand: str
    article: int


card = Card(id=6, brand=obj['selling']['brand_name'], article=obj['nm_id'])
card = card.dict()
#print(card)
