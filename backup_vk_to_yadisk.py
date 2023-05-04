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
    
path_to_file = bya.YaUploader(ya_token)
print(path_to_file.create_folder()['href'])
print()

# for_ya_list = vk.VkPhotosGet(vk_token)
# # for_ya_list.get_url()

# for el in for_ya_list.get_url():
#     date = datetime.utcfromtimestamp(el["date"]).strftime("%Y-%m-%d %H:%M:%S")
#     filename = f'{el["likes"]}_{date}.jpg'
#     f_to_upload = bya.YaUploader(ya_token)
#     # print(ya_token)
#     print()
    
    
