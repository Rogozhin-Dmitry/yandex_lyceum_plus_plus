import calendar
from datetime import date

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


def validate_date(form_obj):
    """Просто охриненный валидатор для дат, умеет всё,
    возвращает либо объект формы с ошибкой, либо нормамльную дату"""
    form_obj.cleaned_data["birthday"] = str(form_obj.cleaned_data["birthday"])
    form_obj.cleaned_data["birthday"] = (
        form_obj.cleaned_data["birthday"]
        .replace(".", "")
        .replace(",", "")
        .replace(" ", "")
        .replace("-", "")
        .replace(":", "")
    )
    moths = {
        "января": "01",
        "февраля": "02",
        "марта": "03",
        "апреля": "04",
        "мая": "05",
        "июня": "06",
        "июля": "07",
        "сентября": "09",
        "октября": "10",
        "ноября": "11",
        "декабря": "12",
        "августа": "08",
    }
    for i in moths:
        if i in form_obj.cleaned_data["birthday"]:
            if not form_obj.cleaned_data["birthday"][:2].isdigit():
                form_obj.cleaned_data["birthday"] = (
                    "0" + form_obj.cleaned_data["birthday"]
                )
            form_obj.cleaned_data["birthday"] = form_obj.cleaned_data[
                "birthday"
            ].replace(i, str(moths[i]))
    if form_obj.cleaned_data["birthday"].isdigit():
        if len(form_obj.cleaned_data["birthday"]) > 8:
            form_obj.add_error(
                "birthday",
                (
                    "Слишком много цифр, попробуйте ввести",
                    " дату в таком формате 01.01.2000",
                ),
            )
            return False, form_obj
        if len(form_obj.cleaned_data["birthday"]) < 8:
            form_obj.add_error(
                "birthday",
                (
                    "Слишком мало цифр, попробуйте ввести",
                    " дату в таком формате 01.01.2000",
                ),
            )
            return False, form_obj
        if len(form_obj.cleaned_data["birthday"]) == 8:
            day, moth, year = (
                int(form_obj.cleaned_data["birthday"][:2]),
                int(form_obj.cleaned_data["birthday"][2:4]),
                int(form_obj.cleaned_data["birthday"][4:]),
            )
            if (
                year > 1900
                and moth in range(13)
                and day <= calendar.monthrange(year, moth)[1]
            ):
                return True, date(day=day, year=year, month=moth)
            moth, day, year = (
                int(form_obj.cleaned_data["birthday"][:2]),
                int(form_obj.cleaned_data["birthday"][2:4]),
                int(form_obj.cleaned_data["birthday"][4:]),
            )
            if (
                year > 1900
                and moth in range(13)
                and day <= calendar.monthrange(year, moth)[1]
            ):
                return True, date(day=day, year=year, month=moth)
            moth, day, year = (
                int(form_obj.cleaned_data["birthday"][:5]),
                int(form_obj.cleaned_data["birthday"][5:6]),
                int(form_obj.cleaned_data["birthday"][6:]),
            )
            if (
                year > 1900
                and moth in range(13)
                and day <= calendar.monthrange(year, moth)[1]
            ):
                return True, date(day=day, year=year, month=moth)
    form_obj.add_error(
        "birthday",
        (
            "Не верный формат даты, попробуйте ввести",
            " дату в таком формате 01.01.2000",
        ),
    )
    return False, form_obj
