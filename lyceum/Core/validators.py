from django.forms import ValidationError


def validate_brilliant(value):
    must_words = ['Превосходно', 'Роскошно']
    if not any(filter(lambda x: x.lower() in value.lower(), must_words)):
        raise ValidationError(f'Обязательно используйте слово {", ".join(must_words)}!')


def count_validator(value):
    if len(value.split()) < 2:
        raise ValidationError(f'Вы должны использывать минимум 2 слова для описания товара')


def star_validator(value):
    if value not in range(1, 6):
        raise ValidationError(f'Оценка может быть только от 1-го до 5-ти')
