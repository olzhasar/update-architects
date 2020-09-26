import factory
from django.contrib.auth.models import User
from django.test import Client


class UserFactory(factory.django.DjangoModelFactory):
    username = "Vincent"
    is_active = True
    is_staff = False

    class Meta:
        model = User
