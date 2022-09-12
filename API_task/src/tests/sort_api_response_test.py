import allure

from API_task.src.utils.helper import Helper
from API_task.src.utils.request_data_from_service import API

h = Helper()
api = API()


@allure.parent_suite("API")
@allure.suite("Mocked API")
@allure.title("Sorted API response")
def test_api_response_filtering():
    # Get data from service:
    with allure.step("Get data from service"):
        response = api.get_request(h.base_url)

    # Get filtered data:
    with allure.step("Get filtered data"):
        filtered_resp = h.filter("price", 0, h.parse_json(response))

    # Sort response filtered data:
    with allure.step("Sort response filtered data"):
        h.sort_by(filtered_resp, "accessibility")

    accessibility = 0

    # Check results:
    with allure.step("Check results"):
        for resp_item in filtered_resp:
            assert resp_item.get("price") != 0
            assert resp_item.get("accessibility") >= accessibility
            accessibility = resp_item.get("accessibility")
