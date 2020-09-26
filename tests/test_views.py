import pytest
from django.test import Client

from tests.fixtures import AdminClient


@pytest.mark.django_db()
def test_home():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_admin():
    client = AdminClient()

    response = client.get("/admin/")

    assert response.status_code == 200
