from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Specialty
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, ListView

from django.utils.text import slugify
from time import time

from statement.models import *
from statement.forms import *


def gen_slug(slug):
    new_slug = slugify(slug, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class HomeView(TemplateView):
    template_name = 'Home/index.html'


@login_required()
def profil_user(request, username):
    try:
        statement = get_object_or_404(Statement, user=request.user)
    except:
        statement = 'Noo'
    return render(request, 'Home/profil_user.html', {'statement': statement, 'form': ReviewForm()})


class SpecialtyView(ListView):
    template_name = 'Home/cource.html'
    queryset = Specialty.objects.all()
    context_object_name = 'courses'


def specialty_single_page(request, slug):
    course = get_object_or_404(Specialty, slug=slug)
    courses = Specialty.objects.all()

    if request.POST.get('btn_remove') == 'Удалить':
        course.delete()
        return redirect('specialty')

    return render(request, 'Home/course-details.html', {'course': course, 'courses': courses})


# регистрация -----
class RegisterFormView(TemplateView):
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            user = User.objects.filter(username=username)
            user_email = User.objects.filter(email=email)

            if user:
                context['username_error'] = 'Пользователь с таким логином уже существует'

            elif user_email:
                context['email_error'] = 'Пользователь с таким Email уже существует'

            elif password != password2:
                context['password2_error'] = 'Пароль не совпадает'

            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                return redirect('/accounts/login/')
        return render(request, self.template_name, context)
