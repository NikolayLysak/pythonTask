import json
from typing import List

from pydantic.main import BaseModel


class Activity(BaseModel):
    activity: str
    type: str
    participants: int
    price: float
    link: str
    key: int
    accessibility: float


class Helper:

    # Parse string to list of Objects:
    @staticmethod
    def parse_to_list_of_objects(response_data: str) -> List[Activity]:
        response = list(map(lambda obj: Activity(**obj), json.loads(response_data)))
        return response

    # Sort data by accessibility
    @staticmethod
    def sort_entries_by_accessibility(unsorted_list: List[Activity], descending=False) -> None:
        unsorted_list.sort(key=lambda obj: obj.accessibility, reverse=descending)

    # Filter response data by price volume
    @staticmethod
    def filter_entries_by_price(volume: float, response: List[Activity]) -> List[Activity]:
        filtered_resp = list(filter(lambda x: (x.price > volume), response))
        return filtered_resp
