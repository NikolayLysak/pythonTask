import configparser

import allure
import pytest

from API_task.src.utils.helper import Helper
from API_task.src.utils.request_data_from_service import API


@pytest.fixture(scope="session")
def prepare_test_data():
    config = configparser.ConfigParser()
    config.read("../../../Config/config.cfg")
    url = config.get("Mocked", "url")
    response = API(url).get_list_of_activities_from_service()
    print("\nThe response has been received successfully")
    yield response
    print("\nTear down test")


@allure.parent_suite("API")
@allure.suite("Mocked API")
@allure.title("Sorted API response")
def test_api_response_filtering(prepare_test_data):
    # Get filtered data:
    with allure.step("Get filtered data"):
        assert len(prepare_test_data) != 0
        filtered_resp = Helper.filter_entries_by_price(0, Helper.parse_to_list_of_objects(prepare_test_data))
        # assert filtered_resp.

    # Sort response filtered data:
    with allure.step("Sort response filtered data"):
        Helper.sort_entries_by_accessibility(filtered_resp)

    with allure.step("Sort response filtered data"):
        print("\n")
        for entry in filtered_resp:
            print(entry.activity, entry.accessibility)
