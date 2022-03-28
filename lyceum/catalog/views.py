from django.shortcuts import render


def item_list(request):
    template = 'catalog/list.html'
    return render(request, template)


def item_detail(request):
    template = 'catalog/detail.html'
    return render(request, template)
