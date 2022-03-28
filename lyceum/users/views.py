from django.shortcuts import render


def user_list(request):
    template = 'users/user_list.html'
    return render(request, template)


def user_detail(request, user_num):
    template = 'users/user_detail.html'
    return render(request, template)


def signup(request):
    template = 'users/signup.html'
    return render(request, template)


def profile(request):
    template = 'users/profile.html'
    return render(request, template)
