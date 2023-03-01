from pprint import pprint

import requests


class YandexDisk:

	def __init__(self, token):
		self.token = token
		self.url = 'https://cloud-api.yandex.net/'

	def get_headers(self):
		return {
			'Content-Type': 'application/json',
			'Authorization': f'OAuth {self.token}'
		}

	def get_files_list(self):
		files_url = f'{self.url}v1/disk/resources/files'
		headers = self.get_headers()
		response = requests.get(url=files_url, headers=headers)
		return response.json()

	def _get_upload_link(self, disk_file_path):
		upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
		headers = self.get_headers()
		params = {"path": disk_file_path, "overwrite": "true"}
		response = requests.get(upload_url, headers=headers, params=params)
		pprint(response.json())
		return response.json()

	def upload_file_to_disk(self, disk_file_path, filename):
		href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
		response = requests.put(href, data=open(filename, 'rb'))
		response.raise_for_status()
		if response.status_code == 201:
			print("Success")


if __name__ == '__main__':
	ya = YandexDisk(token="y0_AgAAAAA3zr2FAADLWwAAAADdYRTJ27waBIkESEmM_j76CebJ_1VrpXo")
	ya.upload_file_to_disk(r"text.txt", filename="text.txt")
	pprint(ya.get_files_list())
