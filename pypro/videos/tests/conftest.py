import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.videos.models.model_video import Video


@pytest.fixture
def video(db):
    return baker.make(Video)


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def response_video_list(client, videos):
    return client.get(reverse('videos:video_list'))


@pytest.fixture
def response_video_item(client, video):
    return client.get(reverse('videos:video_render', args=(video.slug, )))


@pytest.fixture
def response_video_item_fail(client, video):
    return client.get(reverse('videos:video_render', args=(video.slug + '_fail', )))
