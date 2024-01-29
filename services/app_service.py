import requests

class RequestSender:
    def __init__(self, service_url):
        self.service_url = service_url

    def send_user_name(self, name):
        url = f"{self.service_url}/get_user_name"
        response = requests.post(url, json=name)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve user name with status code {response.status_code}")
            return None

    def send_request(self, attributes):
        url = f"{self.service_url}/get_recommendations"
        response = requests.post(url, json=attributes)

        if response.status_code == 200:
            print(response)
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    def send_recommendations_by_download(self, attributes):
        url = f"{self.service_url}/get_recommendations_by_download"
        response = requests.post(url, json=attributes)

        if response.status_code == 200:
            print(response)
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
