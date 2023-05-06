import requests as rq
# import urllib, urllib3
# import urllib.request as ur

# with open('ya_token.txt', 'r') as ya_token_file:
#     ya_token = ya_token_file.read().strip()

# ya_token = ''
    
class YaUploader:
    def __init__(self, ya_token: str):
        self.token = ya_token

    def get_headers(self): 
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_name='VK_PHOTO_BACKUP'):
        create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name}
        create_resp = rq.put(create_folder_url, headers=headers, params=params)
        return create_resp.json()
    
    def get_upload_link(self, folder_name):
        method_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': folder_name, 'overwrite': 'true'}
        response = rq.get(method_url, headers=headers, params=params)
        # print('гет аплоад', response['href'])
        print('get_upload_link', response)
        return response.json()

    def upload(self, photo_url, filename, folder_name='disk/VK_PHOTO_BACKUP'):
        # href = self.get_upload_link(path_to_file=path_to_file).get('href', '')
        headers = self.get_headers()
        params = {'path': '2/img.jpg', 'url': photo_url}
        photo_url = photo_url
        upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = rq.post(url=upload_link, params=params, headers=headers)
        return response
        
        # response.raise_for_status()
        # if response.status_code == 200:
        #     print('Загрузка успешно завершена')
        # if response.status_code == 201:
        #     print('Файл успешно отправлен на загрузку')
# print('тестовый принт', YaUploader(ya_token).create_folder())