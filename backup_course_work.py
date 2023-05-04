import requests as rq
import pprint as pp

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
            'count': 3,
            'extended': 1       # респ возвращает доп поля, в частности likes     
            }
        req = rq.get(download_url, params={**self.params, **download_params}).json()
        for_ya_list = []
        
        # Цикл для выбора максимальной фотки
        for item in req['response']['items']:
            max_photo_size = max(item['sizes'], key=lambda x: vk_photo_types[x['type']])
            for_ya_list.append({'url': max_photo_size['url'], 
                                'type': max_photo_size['type'], 
                                'likes': item['likes']['count'],
                                'id': item['id'],
                                'date': item['date']
                                })
        return for_ya_list



# get_ava = VkPhotosGet(vk_token)
# pp.pprint(get_ava.get_url())  # Сёма - 34872912

# print(ava_df)

# f'{directory}/{i["likes"]}_{datetime.now().strftime("%H-%M-%S")}.jpg'
# f'photo["likes"]["count"]}_{photo["date"]}.jpg'