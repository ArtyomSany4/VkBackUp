import requests as rq

with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()

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
    
    def get_upload_link(self, path_on_yadisk):
        method_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_on_yadisk, 'overwrite': 'true'}
        response = rq.get(method_url, headers=headers, params=params)
        # print('гет аплоад', response['href'])
        return response.json()

    def upload(self, photo_url, filename, folder_name='VK_PHOTO_BACKUP'):
        # href = self.get_upload_link(path_to_file=path_to_file).get('href', '')
        photo_url = photo_url
        folder_name = folder_name
        upload_link = self.get_upload_link(folder_name)['href']
        print(photo_url)
        print(folder_name)
        print(upload_link)
        print()
        response = rq.put(upload_link, data=open(photo_url, 'rb'))
        return response
        
        # response.raise_for_status()
        # if response.status_code == 200:
        #     print('Загрузка успешно завершена')
        # if response.status_code == 201:
        #     print('Файл успешно отправлен на загрузку')
# print('тестовый принт', YaUploader(ya_token).create_folder())