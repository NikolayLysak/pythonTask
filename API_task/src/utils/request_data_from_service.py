import requests as req


class API:
    url: str = None

    def __init__(self, url: str):
        self.url = url

    # Send GET request
    def get_list_of_activities_from_service(self) -> str:
        response = req.get(self.url)
        assert response.status_code == 200
        return response.text
