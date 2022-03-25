from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, item_num):
    return HttpResponse('Подробно элемент')
