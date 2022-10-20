# import requests
#
# from pydantic import BaseModel, ValidationError
#
#
# def pydent(url):
#
#     response = requests.get(url)
#     obj = response.json()
#     return obj
#
#
# class Card(BaseModel):
#     id: int
#     brand: str
#     article: int
#
#
# #url = input()
#
# # card = Card(id=6, brand=pydent('https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json')['selling']['brand_name'],
# #             article=pydent('https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json'
# # )['nm_id'])
# # card = card.dict()
# # print(card)
