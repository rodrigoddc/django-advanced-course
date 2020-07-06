import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture()
def response(client):
    return client.get(reverse('videos:render_video', args=('motivation', )))


def test_status_code(response):
    assert response.status_code == 200


def test_video_title(response):
    assert_contains(response, '<title> Video | Pypro </title>')


def test_video_content(response):
    assert_contains(response, 'src="https://player.vimeo.com/video/435755287"')
