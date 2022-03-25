from django.http import HttpResponse


def user_list(request):
    return HttpResponse('Список пользователей')


def user_detail(request, user_num):
    return HttpResponse('Информация о пользователе')


def signup(request):
    return HttpResponse('Регистрация')


def profile(request):
    return HttpResponse('Мой профиль')
