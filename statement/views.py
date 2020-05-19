from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .service import set_img, reg_number
from .forms import *
from .models import *

from django.utils.text import slugify
from time import time

import transliterate


def gen_slug(first, last):
    try:
        slug = transliterate.translit(f"{first}-{last}", reversed=True)
    except:
        slug = f"{first}-{last}"

    new_slug = slugify(slug, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


def review(request):
    user_id = request.POST.get('user_id')
    statement = get_object_or_404(Statement, pk=int(request.POST.get('statement_id')))
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_form = form.save(commit=False)
            review_form.user = request.user
            review_form.statement = statement
            review_form.save()

    if user_id == 'None':
        return redirect('statement_single_Admin', slug=statement.slug)

    else:
        user = get_object_or_404(User, id=user_id)
        return redirect('profil', username=user.username)


class The_Choice_Admin(LoginRequiredMixin, TemplateView):
    template_name = 'Statement/Admin/The_choice_admin.html'


class The_Choice_Accepted_Admin(LoginRequiredMixin, TemplateView):
    template_name = 'Statement/Admin/The_choice_accepted_admin.html'


class The_Choice_Not_Accepted_Admin(LoginRequiredMixin, TemplateView):
    template_name = 'Statement/Admin/The_choice_not_accepted_admin.html'


# Новые заявлении -----------------------------------------------
class New_Budget_9_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Budget_9/new_9.html'
    queryset = Statement.budget_9.filter(status='В ожидании')
    paginate_by = 20
    context_object_name = 'statements'


class New_Budget_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Budget_11/new_11.html'
    queryset = Statement.objects.filter(Q(budget_contract='Бюджет'), Q(status='В ожидании'),
                                        Q(certificate_status='Аттестат') |
                                        Q(certificate_status='Диплом')).order_by('-created')
    paginate_by = 20
    context_object_name = 'statements'


class New_Contract_9_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Contract_9/new.html'
    queryset = Statement.contact_9.filter(status='В ожидании')
    paginate_by = 20
    context_object_name = 'statements'


class New_Contract_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Contract_11/new.html'
    queryset = Statement.contact_11.filter(status='В ожидании')
    paginate_by = 20
    context_object_name = 'statements'


class New_Corres_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Corres/new.html'
    queryset = Statement.objects.filter(status='В ожидании')
    paginate_by = 20
    context_object_name = 'statements'


# -------------------------------------------------------------------------------------------
class Not_Accepted_Budget_9_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Budget_9/not_accepted.html'
    queryset = Statement.budget_9.filter(status='Не принят')
    paginate_by = 20
    context_object_name = 'statements'


class Not_Accepted_Budget_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Budget_11/not_accepted.html'
    queryset = Statement.objects.filter(Q(budget_contract='Бюджет'), Q(status='Не принят'),
                                        Q(certificate_status='Аттестат') |
                                        Q(certificate_status='Диплом')).order_by('-created')
    paginate_by = 20
    context_object_name = 'statements'


class Not_Accepted_Contract_9_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Contract_9/not_accepted.html'
    queryset = Statement.contact_9.filter(status='Не принят')
    paginate_by = 20
    context_object_name = 'statements'


class Not_Accepted_Contract_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Contract_11/not_accepted.html'
    queryset = Statement.contact_11.filter(status='Не принят')
    paginate_by = 20
    context_object_name = 'statements'


class Not_Accepted_Corres_11_View(LoginRequiredMixin, ListView):
    template_name = 'Statement/Corres/not_accepted.html'
    queryset = Statement.objects.filter(status='Не принят')
    paginate_by = 20
    context_object_name = 'statements'


# Выбор. для заявлении -------------------------------------
class The_Choice(LoginRequiredMixin, TemplateView):
    template_name = 'Statement/Admin/The_choice.html'

    def dispatch(self, request, *args, **kwargs):

        errors = {}

        if request.method == 'POST':
            btn = request.POST.get('BTN')
            if btn == '9-kl':
                radio_budget = request.POST.get('radio-9-forma')
                if radio_budget == 'Бюджет':
                    return redirect('statement_budget_9')
                else:
                    return redirect('statement_contract_9')

            elif btn == '11-kl':
                radio_budget = request.POST.get('radio-11-budget-forma')
                radio_forma = request.POST.get('radio-forma')

                if radio_budget == 'Бюджет' and radio_forma == 'Очный':
                    return redirect('statement_budget_11')

                elif radio_budget == 'Контракт' and radio_forma == 'Очный':
                    return redirect('statement_contract_11')

                elif radio_budget == 'Контракт' and radio_forma == 'Заочный':
                    return redirect('statement_corres_11')

                elif radio_budget == 'Бюджет' and radio_forma == 'Заочный':
                    errors['error'] = "На заочном отделени нет бюджета"

        return render(request, self.template_name, {'errors': errors})


# Добавление Заявлении --------------
@login_required()
def add_statement_budget_9(request):
    stat_1 = Statement.objects.filter(user=request.user)
    errors = {}
    if stat_1:
        errors['error'] = 'Yes'
    else:
        errors['error'] = 'Noo'

    specialty = request.POST.get('specialty')
    nationality = request.POST.get('nationality')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.slug = gen_slug(statement.first_name, statement.last_name)
            statement.budget_contract = 'Бюджет'
            statement.specialty = specialty
            statement.nationality = nationality
            statement.save()
            return redirect('profil', request.user)
    else:
        form = StatementForm()
    return render(request, 'Statement/Budget_9/add_statement_budget_9.html', {'form': form, 'errors': errors})


@login_required()
def add_statement_budget_11(request):
    stat_1 = Statement.objects.filter(user=request.user)
    errors = {}
    if stat_1:
        errors['error'] = 'Yes'
    else:
        errors['error'] = 'Noo'

    certificate_status = request.POST.get('certificate_status')
    specialty = request.POST.get('specialty')
    nationality = request.POST.get('nationality')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.slug = gen_slug(statement.first_name, statement.last_name)
            statement.budget_contract = 'Бюджет'
            statement.specialty = specialty
            statement.nationality = nationality
            statement.certificate_status = certificate_status
            statement.save()
            return redirect('profil', request.user)
    else:
        form = StatementForm()
    return render(request, 'Statement/Budget_11/add_statement_budget_11.html', {'form': form, 'errors': errors})


@login_required()
def add_statement_contract_9(request):
    stat_1 = Statement.objects.filter(user=request.user)
    errors = {}
    if stat_1:
        errors['error'] = 'Yes'
    else:
        errors['error'] = 'Noo'

    specialty = request.POST.get('specialty')
    nationality = request.POST.get('nationality')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.slug = gen_slug(statement.first_name, statement.last_name)
            statement.budget_contract = 'Контракт'
            statement.specialty = specialty
            statement.nationality = nationality
            statement.save()
            return redirect('profil', request.user)
    else:
        form = StatementForm()
    return render(request, 'Statement/Contract_9/add_statement_contract_9.html', {'form': form, 'errors': errors})


@login_required()
def add_statement_contract_11(request):
    stat_1 = Statement.objects.filter(user=request.user)
    errors = {}
    if stat_1:
        errors['error'] = 'Yes'
    else:
        errors['error'] = 'Noo'

    certificate_status = request.POST.get('certificate_status')
    specialty = request.POST.get('specialty')
    nationality = request.POST.get('nationality')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.slug = gen_slug(statement.first_name, statement.last_name)
            statement.budget_contract = 'Контракт'
            statement.certificate_status = certificate_status
            statement.nationality = nationality
            statement.specialty = specialty
            statement.save()
            return redirect('profil', request.user)
    else:
        form = StatementForm()
    return render(request, 'Statement/Contract_11/add_statement_contract_11.html', {'form': form, 'errors': errors})


@login_required()
def add_statement_corres_11(request):
    stat_1 = Statement.objects.filter(user=request.user)
    errors = {}
    if stat_1:
        errors['error'] = 'Yes'
    else:
        errors['error'] = 'Noo'

    certificate_status = request.POST.get('certificate_status')
    specialty = request.POST.get('specialty')
    nationality = request.POST.get('nationality')
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.user = request.user
            statement.slug = gen_slug(statement.first_name, statement.last_name)
            statement.budget_contract = 'Контракт'
            statement.form_training = 'Заочный'
            statement.certificate_status = certificate_status
            statement.nationality = nationality
            statement.specialty = specialty
            statement.save()
            return redirect('profil', request.user)
    else:
        form = StatementForm()
    return render(request, 'Statement/Corres/add_statement_corres_11.html', {'form': form, 'errors': errors})


# Пагинатор -------------------
def paginator_fun(object_list, request):
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        statements = paginator.page(page)
    except PageNotAnInteger:
        statements = paginator.page(1)
    except EmptyPage:
        statements = paginator.page(paginator.num_pages)

    return statements


# Распридление по специальности (принятые)-------------------------------------------------------------
@login_required()
def the_accepted(request, title):
    if title == 'tm-budget-9':
        object_list = Statement.budget_9.filter(status='Принят', specialty='Технология машиностроения')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Технология машиностроения'})

    elif title == 'tes-budget-9':
        object_list = Statement.budget_9.filter(status='Принят', specialty='Тепловые электрические станции')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Тепловые электрические станции'})

    elif title == 'est-budget-9':
        object_list = Statement.budget_9.filter(status='Принят', specialty='Электрические станции, сети и системы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электрические станции, сети и системы'})

    elif title == 'es-budget-9':
        object_list = Statement.budget_9.filter(status='Принят', specialty='Электроснабжение (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электроснабжение (по отраслям)'})

    elif title == 'asoi-budget-11':
        object_list = Statement.objects.filter(status='Принят', budget_contract='Бюджет',
                                                specialty='Автоматизированные системы обработки информации и управления')
        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Автоматизированные системы обработки информации и управления'})

    # 9 Класс Контракт ------------------------------------------------------------
    elif title == 'tm-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Технология машиностроения')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Технология машиностроения'})

    elif title == 'sp-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Сварочное производство')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Сварочное производство'})

    elif title == 'po-contract-9':
        object_list = Statement.contact_9.filter(status='Принят',
                                                 specialty='Программное обеспечение вычислительной техники и автоматизированных систем')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Программное обеспечение вычислительной техники и автоматизированных систем'})

    elif title == 'to-contract-9':
        object_list = Statement.contact_9.filter(status='Принят',
                                                 specialty='Техническое обслуживание средств вычислительной техники и компьютерных сетей')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Техническое обслуживание средств вычислительной техники и компьютерных сетей'})

    elif title == 'asoi-contract-9':
        object_list = Statement.contact_9.filter(status='Принят',
                                                 specialty='Автоматизированные системы обработки информации и управления')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Автоматизированные системы обработки информации и управления'})

    elif title == 'tes-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Тепловые электрические станции')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Тепловые электрические станции'})

    elif title == 'est-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Электрические станции, сети и системы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электрические станции, сети и системы'})

    elif title == 'es-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Электроснабжение (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электроснабжение (по отраслям)'})

    elif title == 'gr-contract-9':
        object_list = Statement.contact_9.filter(status='Принят', specialty='Открытые горные работы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Открытые горные работы'})

    elif title == 'ebu-contract-9':
        object_list = Statement.contact_9.filter(status='Принят',
                                                 specialty='Экономика и бухгалтерский учет (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Экономика и бухгалтерский учет (по отраслям)'})

    # 11 Класс Контракт ------------------------------------------------------------
    elif title == 'tm-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Технология машиностроения')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Технология машиностроения'})

    elif title == 'sp-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Сварочное производство')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Сварочное производство'})

    elif title == 'po-contract-11':
        object_list = Statement.contact_11.filter(status='Принят',
                                                 specialty='Программное обеспечение вычислительной техники и автоматизированных систем')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Программное обеспечение вычислительной техники и автоматизированных систем'})

    elif title == 'to-contract-11':
        object_list = Statement.contact_11.filter(status='Принят',
                                                 specialty='Техническое обслуживание средств вычислительной техники и компьютерных сетей')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Техническое обслуживание средств вычислительной техники и компьютерных сетей'})

    elif title == 'asoi-contract-11':
        object_list = Statement.contact_11.filter(status='Принят',
                                                 specialty='Автоматизированные системы обработки информации и управления')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Автоматизированные системы обработки информации и управления'})

    elif title == 'tes-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Тепловые электрические станции')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Тепловые электрические станции'})

    elif title == 'est-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Электрические станции, сети и системы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электрические станции, сети и системы'})

    elif title == 'es-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Электроснабжение (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электроснабжение (по отраслям)'})

    elif title == 'gr-contract-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Открытые горные работы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Открытые горные работы'})

    elif title == 'ebu-contract-11':
        object_list = Statement.contact_11.filter(status='Принят',
                                                 specialty='Экономика и бухгалтерский учет (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Экономика и бухгалтерский учет (по отраслям)'})

    # 11 Класс Контракт Заочный ------------------------------------------------------------
    elif title == 'tm-corres-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Технология машиностроения')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Технология машиностроения'})

    elif title == 'po-corres-11':
        object_list = Statement.contact_11.filter(status='Принят',
                                                  specialty='Программное обеспечение вычислительной техники и автоматизированных систем')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Программное обеспечение вычислительной техники и автоматизированных систем'})

    elif title == 'tes-corres-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Тепловые электрические станции')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Тепловые электрические станции'})

    elif title == 'est-corres-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Электрические станции, сети и системы')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электрические станции, сети и системы'})

    elif title == 'es-corres-11':
        object_list = Statement.contact_11.filter(status='Принят', specialty='Электроснабжение (по отраслям)')

        return render(request, 'Statement/Admin/accepted.html', {'statements': paginator_fun(object_list, request),
                                                                 'title': 'Электроснабжение (по отраслям)'})



# --- Single page i Принять Не принять и добавить регистрационный номер
@login_required()
def statement_single_Admin(request, slug):

    user_statement = get_object_or_404(Statement, slug=slug)

    if request.method == 'POST':
        btn = request.POST.get('btn-accept')
        if btn == 'Принять заявление':
            responsible = f'{request.user.last_name} {request.user.first_name}'
            user_statement.responsible = responsible
            user_statement.status = 'Принят'

            if user_statement.specialty == 'Технология машиностроения' and user_statement.budget_contract == 'Бюджет':
                try:
                    count_reg = Statement.budget_9.filter(specialty='Технология машиностроения',
                                                          status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                user_statement.save()
                reg_number.reg_numbr_certificate(user_statement, 'ТМ', '1', 'Бюджет')

            if user_statement.specialty == 'Тепловые электрические станции' and user_statement.budget_contract == 'Бюджет':
                try:
                    count_reg = Statement.budget_9.filter(specialty='Тепловые электрические станции',
                                                         status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТЭС', '1', 'Бюджет')

            if user_statement.specialty == 'Электрические станции, сети и системы' \
                    and user_statement.budget_contract == 'Бюджет':
                try:
                    count_reg = Statement.budget_9.filter(specialty='Электрические станции, сети и системы',
                                                          status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭСТ', '1', 'Бюджет')

            if user_statement.specialty == 'Электроснабжение (по отраслям)' \
                    and user_statement.budget_contract == 'Бюджет':
                try:
                    count_reg = Statement.budget_9.filter(specialty='Электроснабжение (по отраслям)',
                                                          status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭС', '1', 'Бюджет')

            if user_statement.specialty == 'Автоматизированные системы обработки информации и управления' \
                    and user_statement.budget_contract == 'Бюджет':
                try:
                    count_reg = Statement.objects.filter(specialty='Автоматизированные системы обработки информации и управления',
                                                         budget_contract='Бюджет',
                                                         status='Принят')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'АСОИ', '2', 'Бюджет')

            # 9 Класс Контракт ------------------------------------------------------------
            if user_statement.specialty == 'Технология машиностроения' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Технология машиностроения',
                                                         status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТМ', '1')

            if user_statement.specialty == 'Сварочное производство' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Сварочное производство',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()


                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'СП', '1')

            if user_statement.specialty == 'Программное обеспечение вычислительной техники и автоматизированных систем' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Программное обеспечение вычислительной техники и автоматизированных систем',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ПО', '1')

            if user_statement.specialty == 'Техническое обслуживание средств вычислительной техники и компьютерных сетей' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Техническое обслуживание средств вычислительной техники и компьютерных сетей',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТО', '1')

            if user_statement.specialty == 'Автоматизированные системы обработки информации и управления' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Автоматизированные системы обработки информации и управления',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'АСОИ', '1')

            if user_statement.specialty == 'Тепловые электрические станции' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Тепловые электрические станции',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТЭС', '1')

            if user_statement.specialty == 'Электрические станции, сети и системы' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Электрические станции, сети и системы',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭСТ', '1')

            if user_statement.specialty == 'Электроснабжение (по отраслям)' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Электроснабжение (по отраслям)',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭС', '1')

            if user_statement.specialty == 'Открытые горные работы' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Открытые горные работы',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ГР', '1')

            if user_statement.specialty == 'Экономика и бухгалтерский учет (по отраслям)' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.certificate_status == 'Свидетельство':
                try:
                    count_reg = Statement.contact_9.filter(specialty='Экономика и бухгалтерский учет (по отраслям)',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'БУ', '1')

            # 11 Класс Контракт Очный ------------------------------------------------------------
            if user_statement.specialty == 'Технология машиностроения' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Технология машиностроения',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТМ', '2')

            if user_statement.specialty == 'Сварочное производство' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Сварочное производство',
                                                            status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()


                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'СП', '2')

            if user_statement.specialty == 'Программное обеспечение вычислительной техники и автоматизированных систем' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Программное обеспечение вычислительной техники и автоматизированных систем',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ПО', '2')

            if user_statement.specialty == 'Техническое обслуживание средств вычислительной техники и компьютерных сетей' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Техническое обслуживание средств вычислительной техники и компьютерных сетей',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТО', '2')

            if user_statement.specialty == 'Автоматизированные системы обработки информации и управления' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Автоматизированные системы обработки информации и управления',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'АСОИ', '2')

            if user_statement.specialty == 'Тепловые электрические станции' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Тепловые электрические станции',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТЭС', '2')

            if user_statement.specialty == 'Электрические станции, сети и системы' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Электрические станции, сети и системы',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭСТ', '2')

            if user_statement.specialty == 'Электроснабжение (по отраслям)' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Принят'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Электроснабжение (по отраслям)',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭС', '2')

            if user_statement.specialty == 'Открытые горные работы' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Открытые горные работы',
                                                            status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ГР', '2')

            if user_statement.specialty == 'Экономика и бухгалтерский учет (по отраслям)' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Очный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.contact_11.filter(specialty='Экономика и бухгалтерский учет (по отраслям)',
                                                            status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'БУ', '2')

            # 11 Класс Контракт Заочный ------------------------------------------------------------
            if user_statement.specialty == 'Технология машиностроения' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Заочный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.corres_11.filter(specialty='Технология машиностроения',
                                                           status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТМ', '2', corres='Заочный')

            if user_statement.specialty == 'Программное обеспечение вычислительной техники и автоматизированных систем' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Заочный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.corres_11.filter(specialty='Программное обеспечение вычислительной техники и автоматизированных систем',
                                                           status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ПО', '2', corres='Заочный')

            if user_statement.specialty == 'Тепловые электрические станции' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Заочный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.corres_11.filter(specialty='Тепловые электрические станции',
                                                           status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ТЭС', '2', corres='Заочный')

            if user_statement.specialty == 'Электрические станции, сети и системы' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Заочный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.corres_11.filter(specialty='Электрические станции, сети и системы',
                                                           status='Принят').order_by('-reg_number')[0:1].get()

                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭСТ', '2', corres='Заочный')

            if user_statement.specialty == 'Электроснабжение (по отраслям)' \
                    and user_statement.budget_contract == 'Контракт' \
                    and user_statement.form_training == 'Заочный' \
                    and (user_statement.certificate_status == 'Аттестат'
                         or user_statement.certificate_status == 'Диплом'):
                try:
                    count_reg = Statement.corres_11.filter(specialty='Электроснабжение (по отраслям)',
                                                           status='Принят').order_by('-reg_number')[0:1].get()
                    user_statement.reg_number = int(count_reg.reg_number) + 1
                    user_statement.created_the_accepted = timezone.now()

                except:
                    user_statement.reg_number = 1
                    user_statement.created_the_accepted = timezone.now()

                reg_number.reg_numbr_certificate(user_statement, 'ЭС', '2', corres='Заочный')

        elif btn == 'Не принят':
            responsible = f'{request.user.last_name} {request.user.first_name}'
            user_statement.responsible = responsible
            user_statement.status = 'Не принят'
            user_statement.reg_number = 0
            user_statement.registor_index = 'Не принят'
            user_statement.created_the_accepted = timezone.now()
            user_statement.save()

    return render(request, 'Statement/Admin/statement_single_page.html',
                  {'statement': user_statement,
                   'form': ReviewForm()})

