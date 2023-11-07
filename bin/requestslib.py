import requests

class Requests:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers)
        return response

    def put_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}
        response = requests.put(url, json=data, headers=headers)
        return response

    def delete_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response