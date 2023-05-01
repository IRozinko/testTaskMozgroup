import requests
import pytest

BASE_URL = "http://demo8955896.mockable.io"
members_method = "/members"


@pytest.fixture
def get_response_data():
    response = requests.get(BASE_URL + members_method)
    return response


def test_get_members_status_code(get_response_data):
    assert get_response_data.status_code == 200, f"Expected status code 200, but received {get_response_data.status_code}"


def test_get_members_response_content(get_response_data):
    response_body = get_response_data.json()

    assert response_body["status"] == "success", "Status should be 'success'"
    assert "data" in response_body, "Response should contain 'data'"
    assert "members" in response_body["data"], "Data should contain 'members'"

    members = response_body["data"]["members"]
    assert len(members) > 0, "Members list should not be empty"

    for any_member in members:
        assert "position" in any_member, "Member should have a position field"
        assert "level" in any_member, "Member should have a level field"
        assert "first_name" in any_member, "Member should have a first_name field"
        assert "last_name" in any_member, "Member should have a last_name field"
        assert "day_birth" in any_member, "Member should have a day_birth field"
        assert "hr_department" in any_member, "Member should have an hr_department field"
        assert "email" in any_member, "Member should have an email field"
        assert "mobile" in any_member, "Member should have a mobile field"
        assert "probation_period" in any_member, "Member should have a probation_period field"
        assert "ID" in any_member, "Member should have an ID field"


def test_member_status_code_and_content():
    response = requests.get(f"{BASE_URL}/member/025a626c4c9c")
    assert response.status_code == 200, "Status code should be 200"

    response_body = response.json()
    assert response_body["status"] == "success", "Status should be 'success'"
    assert "data" in response_body, "Response should contain 'data'"

    member = response_body["data"]
    assert "position" in member, "Member should have a position field"
    assert "level" in member, "Member should have a level field"
    assert "first_name" in member, "Member should have a first_name field"
    assert "last_name" in member, "Member should have a last_name field"
    assert "day_birth" in member, "Member should have a day_birth field"
    assert "hr_department" in member, "Member should have an hr_department field"
    assert "email" in member, "Member should have an email field"
    assert "mobile" in member, "Member should have a mobile field"
    assert "probation_period" in member, "Member should have a probation_period field"
    assert "ID" in member, "Member should have an ID field"
