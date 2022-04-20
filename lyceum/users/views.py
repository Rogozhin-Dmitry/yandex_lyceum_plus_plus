from django import forms
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from rating.models import Rating

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Почта')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )


@login_required
def user_list(request):
    users = (
        User.objects.select_related("profile")
            .only('profile__birthday', 'first_name', 'last_name')
            .all()
    )
    TEMPLATE = "users/user_list.html"
    context = {
        "users": users,
    }
    return render(request, TEMPLATE, context)


@login_required
def user_detail(request, user_num):
    user = get_object_or_404(
        User.objects.select_related("profile")
            .filter(id=user_num)
            .only('profile__birthday', 'first_name', 'last_name', 'email'),
    )

    favourite_items = Rating.objects.get_favourite_rating_form_user_id(
        user_num
    )
    context = {'user': user, 'favourite_items': favourite_items}
    TEMPLATE = "users/user_detail.html"
    return render(request, TEMPLATE, context)


def signup(request):
    TEMPLATE = "users/signup.html"
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, TEMPLATE, context)


@login_required
def profile(request):
    TEMPLATE = "users/profile.html"
    user = get_object_or_404(
        User.objects.select_related("profile")
            .filter(id=request.user.id)
            .only('profile__birthday', 'first_name', 'last_name', 'email'),
    )

    favourite_items = Rating.objects.get_favourite_rating_form_user_id(
        request.user.id
    )
    form = UserUpdateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save(update_fields=['email', 'first_name', 'last_name'])
            return redirect('profile')
    context = {'form': form, 'user': user, 'favourite_items': favourite_items}
    return render(request, TEMPLATE, context)
