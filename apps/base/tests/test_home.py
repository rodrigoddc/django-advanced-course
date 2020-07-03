from django.test import Client

# from pypro.django_assertions import assert_contains


def test_status_code(client: Client):
    response = client.get('/home')
    assert response.status_code == 200 or 301


# def test_title_home(client: Client):
#     response = client.get('/home')
#     assert_contains(response, '<title> Home | Pypro </title>')
