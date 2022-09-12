import json


class Helper:
    base_url = "https://587ec89e-2eb8-41a0-b858-5d9cfdc428ba.mock.pstmn.io/api/activity"

    # Parse string to JSON
    def parse_json(self, data: str) -> list:
        return json.loads(data)

    # Sort data by key
    def sort_by(self, unsorted_list: list, key_name: str, descending=False) -> None:
        unsorted_list.sort(key=lambda obj: obj.get(key_name), reverse=descending)

    # Filter response data by price volume
    def filter(self, key: str, volume: float, resp: list) -> list:
        filtered_resp = []

        for resp_item in resp:
            if resp_item.get('price') > 0:
                filtered_resp.append(resp_item)

        return filtered_resp
