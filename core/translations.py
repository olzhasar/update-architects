from django.utils.translation import get_language


class TranslationDescriptor:
    default_prefix = "ru"

    def __init__(self, instance, locale):
        prefix_mapping = {"ru-ru": "ru", "en-us": "en"}
        self.instance = instance
        self.prefix = prefix_mapping.get(locale, "ru")

    def __getattr__(self, field_name):
        translated_field = f"{self.prefix}_{field_name}"
        if hasattr(self.instance, translated_field):
            val = getattr(self.instance, translated_field)
            if val:
                return val
            untranslated_field = f"{self.default_prefix}_{field_name}"
            if hasattr(self.instance, untranslated_field):
                return getattr(self.instance, untranslated_field)
        return getattr(self.instance, field_name)

    def __str__(self):
        return str(self.instance)


class TranslationProxy:
    def __get__(self, instance, owner):
        locale = get_language()
        return TranslationDescriptor(instance, locale)
