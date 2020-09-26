from django.test import Client

from tests.factories import UserFactory


class AdminClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = UserFactory(is_staff=True, is_superuser=True)
        self.force_login(user)
