import backup_course_work as vk
import backup_ya_api as bya
# import datetime
from datetime import datetime


# vk_user_id = input('Укажите айди пользователя ВК: ')
# ya_token = input('Укажите токен с Полигона Яндекс.Диска: ')

with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()
with open('vk_token.txt', 'r') as vk_token_file:
    vk_token = vk_token_file.read().strip()
    
# href_for_path = bya.YaUploader(ya_token)

# Создаем папку на ядиске (если не передать имя, 
# то в имя пихнет VK_PHOTO_BACKUP)
folder_name = input('Введите имя папки: ')
# path_on_yadisk = bya.YaUploader(ya_token).create_folder(yad_folder_name)
# print(path_on_yadisk)

# Получаем список фоток для загрузки
for_ya_list = vk.VkPhotosGet(vk_token)

# Цикл для каждой фотки
for el in for_ya_list.get_url():
    date = datetime.utcfromtimestamp(el["date"]).strftime("%Y-%m-%d %H_%M_%S")
    filename = f'{el["likes"]}_05.jpg'
    photo_url = el['url']
    f_to_upload = bya.YaUploader(ya_token) # хз, зачем это
    f_to_upload.upload(photo_url, filename, folder_name)
    # print(ya_token)
    print()
    
    
# path_to_file, filename