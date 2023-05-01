import json
import pandas as pd
import requests as rq

# Получаем токены из файликов
with open('vk_token.txt', 'r') as vk_token_file:
    vk_token = vk_token_file.read().strip()
with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()

# Разобраться с токеном ВК, он, похоже, не нужен


# Функция загрузки из ВК
class VkPhotosGet:  
    # Пользак должен ввести токен яндекса и ид пользака вк
    # ya_token = input('Укажите токен с полигона Я.Диска: ')
    url = 'https://api.vk.com/method/'
    def __init__(self, vk_token):
        self.params = {
            'access_token': vk_token,
            'v':'5.131'
            }
    
    def get_url(self, owner_id=None):
        vk_photo_types = {
            'w': 10, 'z': 9, 'y': 8, 'r': 7, 'q': 6, 'p': 5, 'o': 4, 'x':3, 'm': 2, 's': 1}        
        # ava_df = pd.DataFrame()
        download_url = self.url + 'photos.get'
        download_params = {
            'owner_id': owner_id, # если не объявлен дополнительно, определит по владельцу токена
            'album_id': 'profile', # служебный альбом, только авы
            # 'photo_sizes': '', разобраться,
            'count': 10,
            'extended': 1            
            }
        req = rq.get(download_url, params={**self.params, **download_params}).json()
        for_logs = []
        max_photo_dict = {} # Словарь кол-во лайков: урл на макстип фото
        # Цикл для выбора максимальной фотки
        for item in req['response']['items']:
            # max_photo_size = pd.DataFrame([max(item['sizes'], key=lambda x: vk_photo_types[x["type"]])])
            max_photo_size = max(item['sizes'], key=lambda x: vk_photo_types[x["type"]])
            for_logs.append({'file_name': item['likes']['count'], 'type': max_photo_size['type']}) # откуда-то берется ноль для типа фото
            # print(max_photo_size)
            print()
            print()
            print(for_logs)     


        # ava_df = pd.DataFrame(req['response']['items'][0]['sizes'])
        # print(req)
        # return ava_df



get_ava = VkPhotosGet(vk_token)
print(get_ava.get_url()) # Сёма - 34872912
# ava_df = pd.concat([ava_df, pd.DataFrame(get_ava['response']['items'])])

# print(ava_df)


