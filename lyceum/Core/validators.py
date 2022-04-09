from django.forms import ValidationError


def validate_brilliant(value):
    must_words = ["Превосходно", "Роскошно"]
    if not any(filter(lambda x: x.lower() in value.lower(), must_words)):
        raise ValidationError(
            f'Обязательно используйте слово {", ".join(must_words)}!'
        )


def count_validator(value):
    if len(value.split()) < 2:
        raise ValidationError(
            "Вы должны использывать минимум 2 слова для описания товара"
        )
