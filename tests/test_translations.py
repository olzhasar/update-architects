import pytest

from core.translations import TranslationProxy


@pytest.fixture
def mock_get_language(mocker):
    mock = mocker.patch("core.translations.get_language")
    return mock


class A:
    field_ru = 5
    field_en = 8

    field_2_ru = 10
    field_2_en = ""

    translated = TranslationProxy()

    untranslated_field = 20


def test_descriptor(mock_get_language):
    mock_get_language.return_value = "en"

    a = A()
    assert a.translated.field == 8
    assert a.translated.field_2 == 10
    assert a.untranslated_field == 20
