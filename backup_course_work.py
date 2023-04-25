import json
import pandas as pd
import requests as rq
import pprint

# Получаем токены из файликов
with open('vk_token.txt', 'r') as vk_token_file:
    vk_token = vk_token_file.read().strip()
with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()

# Функция загрузки из ВК
class VkApi:
    url = 'https://api.vk.com/method/'
    def __init__(self, vk_token):
        self.params = {
            'access_token': vk_token,
            'v':'5.131'
            }
    
    def download(self, owner_id=None):
        ava_df = pd.DataFrame()
        download_url = self.url + 'photos.get'
        download_params = {
            'owner_id': owner_id, # если не объявлен дополнительно, определит по владельцу токена
            'album_id': 'profile', # служебный альбом, только авы
            # 'photo_sizes': '', разобраться,
            'count': 3,
            'extended': 1            
            }
        req = rq.get(download_url, params={**self.params, **download_params}).json()
        # Тут нужен цикл, чтобы добавлять в датафрейм строки с ссылкой на 
        # максимальный размер фото (тип W)
        ava_df = pd.DataFrame(req['response']['items'][0]['sizes'])
        print(req)
        return ava_df



get_ava = VkApi(vk_token)
print(get_ava.download()) # Сёма - 34872912
# ava_df = pd.concat([ava_df, pd.DataFrame(get_ava['response']['items'])])

# print(ava_df)


