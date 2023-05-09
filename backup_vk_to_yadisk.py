import backup_vk_api as vk
import backup_ya_api as bya
import json
from datetime import datetime

with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()
with open('vk_token.txt', 'r') as vk_token_file:
    vk_token = vk_token_file.read().strip()
    
# vk_user_id = input('Укажите айди пользователя ВК: ')
# ya_token = input('Укажите токен с Полигона Яндекс.Диска: ')

# Создаем папку на ядиске (если не передать имя, 
# то в имя пихнет VK_PHOTO_BACKUP)
folder_name = input('Введите имя папки: ')
if len(folder_name) == 0:
    folder_name = 'VK_PHOTO_BACKUP'
path_on_yadisk = bya.YaUploader(ya_token).create_folder(folder_name)

# Получаем список фоток для загрузки
owner_id = input('Укажите ИД пользователя: ')
if len(owner_id) == 0:
    owner_id = None
for_ya_list = vk.VkPhotosGet(vk_token)
photo_count = input('Укажите количество фотографий для сохранения: ')
if len(photo_count) == 0:
    photo_count = 5

upload_log = [] # Пустой список, в него собираем инфу для лога
# Цикл для каждой фотки
for el in for_ya_list.get_url(photo_count, owner_id):
    date = datetime.utcfromtimestamp(el["date"]).strftime("%Y-%m-%d %H_%M_%S")
    filename = f'{el["likes"]}_{date}.jpg'
    photo_url = el['url']
    f_to_upload = bya.YaUploader(ya_token) 
    f_to_upload.upload(photo_url, filename, folder_name)
    
    # Теперь собираем лог
    to_log_dict = {'file_name': filename, 'size': el['type']}
    upload_log.append(to_log_dict)
    print()
    
# Экспортируем лог в json файл
with open('backup_log_file.json', 'w') as f:
    json.dump(upload_log, f)