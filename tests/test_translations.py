import pytest

from core.translations import TranslationProxy


@pytest.fixture
def mock_get_language(mocker):
    mock = mocker.patch("core.translations.get_language")
    return mock


class A:
    ru_field = 5
    en_field = 8

    ru_field_2 = 10
    en_field_2 = ""

    translated = TranslationProxy()

    untranslated_field = 20


def test_descriptor(mock_get_language):
    mock_get_language.return_value = "en-us"

    a = A()
    assert a.translated.field == 8
    assert a.translated.field_2 == 10
    assert a.untranslated_field == 20
