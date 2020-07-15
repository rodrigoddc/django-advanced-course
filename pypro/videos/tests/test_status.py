def test_item_status_code(response_video_item):
    assert response_video_item.status_code == 200


def test_item_status_code_fail(response_video_item_fail):
    assert response_video_item_fail.status_code == 404


def test_list_status_code(response_video_list):
    assert response_video_list.status_code == 200
