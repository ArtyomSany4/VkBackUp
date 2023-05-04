import requests as rq

# token = ''
with open('ya_token.txt', 'r') as ya_token_file:
    ya_token = ya_token_file.read().strip()
    
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
    
    def _get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = rq.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file, filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(path_to_file=path_to_file).get('href', '')
        response = rq.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 200:
            print('Загрузка успешно завершена')
        if response.status_code == 201:
            print('Файл успешно отправлен на загрузку')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'путь'
    token = ya_token
    path = YaUploader(token)
    result = path.create_folder(path_to_file)
    
    # print(result)