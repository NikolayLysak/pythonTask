import requests as req


class API:

    # Send GET request
    def get_request(self, url) -> str:
        response = req.get(url)
        return response.text
