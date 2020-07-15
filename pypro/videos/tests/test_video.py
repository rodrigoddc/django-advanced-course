from django.urls import reverse

from pypro.django_assertions import assert_contains


def test_video_title(response_video_list, videos):
    for video in videos:
        assert_contains(response_video_list, video.title)


def test_video_link(response_video_list, client, videos):
    for video in videos:
        video_link = reverse('videos:video_render', args=(video.slug, ))
        assert_contains(response_video_list, video_link)


def test_video_content(response_video_item, video):
    assert_contains(response_video_item, f'src="https://player.vimeo.com/video/{ video.vimeo_id }"')
