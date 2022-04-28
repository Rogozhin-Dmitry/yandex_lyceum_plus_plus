from Core.validators import validate_date
from django import forms
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from rating.models import Rating
from django.views.generic import TemplateView

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Почта', max_length=256)


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Почта')
    birthday = forms.CharField(label='День рождения')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )


class UserList(LoginRequiredMixin, TemplateView):
    TEMPLATE = "users/user_list.html"

    def get(self, request, *args, **kwargs):
        users = (
            User.objects.select_related("profile")
            .only('profile__birthday', 'first_name', 'last_name')
            .all()
        )
        context = {
            "users": users,
        }
        return render(request, self.TEMPLATE, context)


class UserDetail(LoginRequiredMixin, TemplateView):
    TEMPLATE = "users/user_detail.html"

    def get(self, request, user_num='0', *args, **kwargs):
        user = get_object_or_404(
            User.objects.select_related("profile")
            .filter(id=user_num)
            .only('profile__birthday', 'first_name', 'last_name', 'email'),
        )
        favourite_items = Rating.objects.get_favourite_rating_form_user_id(
            user_num
        )
        context = {'user': user, 'favourite_items': favourite_items}
        return render(request, self.TEMPLATE, context)


class SignUp(LoginRequiredMixin, TemplateView):
    TEMPLATE = "users/signup.html"

    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, self.TEMPLATE, context)

    def post(self, request):
        form = RegisterForm(request.POST or None)
        context = {
            'form': form,
        }
        if form.is_valid():
            if (
                User.objects.filter(email=form.cleaned_data['email'])
                .only('id')
                .first()
            ):
                form.add_error('email', "Эта почта уже занята")
                return render(request, self.TEMPLATE, context)
            form.save()
            return redirect('login')


class Profile(LoginRequiredMixin, TemplateView):
    TEMPLATE = "users/profile.html"

    def get_context_data(self, request, **kwargs):
        user = get_object_or_404(
            User.objects.select_related("profile")
            .filter(id=request.user.id)
            .only('profile__birthday', 'first_name', 'last_name', 'email'),
        )

        favourite_items = Rating.objects.get_favourite_rating_form_user_id(
            request.user.id
        )
        form = UserUpdateForm(
            request.POST or None, initial={'email': user.email}
        )
        return {'form': form, 'user': user, 'favourite_items': favourite_items}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, self.TEMPLATE, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        form, user = context['form'], context['user']
        if form.is_valid():
            user_edit = (
                User.objects.filter(email=form.cleaned_data['email'])
                .only('id')
                .first()
            )
            if user_edit.id != user.id:
                form.add_error('email', "Эта почта уже занята")
                return render(request, self.TEMPLATE, context)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']

            if not form.cleaned_data["birthday"]:
                user.save(update_fields=["email", "first_name", "last_name"])
                return redirect("profile")

            valid_date = validate_date(form)
            if not valid_date[0]:
                context['form'] = valid_date[1]
                return render(request, self.TEMPLATE, context)

            user.profile.birthday = valid_date[1]
            user.profile.save()
            user.save(update_fields=['email', 'first_name', 'last_name'])
            return redirect('profile')
