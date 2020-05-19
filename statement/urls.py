from django.urls import path
from .views import *


urlpatterns = [
    path('', The_Choice.as_view(), name='the_choice'),
    path('add/review/', review, name='review'),
    path('admin/', The_Choice_Admin.as_view(), name='the_choice_admin'),

    # ==== single page
    path('single/<slug>', statement_single_Admin, name='statement_single_Admin'),
    path('accepted/<title>', the_accepted, name='statement_single_accepted'),

    # ==== Новые заявлении
    path('new/', The_Choice_Accepted_Admin.as_view(), name='The_Choice_Accepted_Admin'),
    path('new/budget/9/', New_Budget_9_View.as_view(), name='new_budget_9'),
    path('new/budget/11/', New_Budget_11_View.as_view(), name='new_budget_11'),
    path('new/contract/9/', New_Contract_9_View.as_view(), name='new_contract_9'),
    path('new/contract/11/', New_Contract_11_View.as_view(), name='new_contract_11'),
    path('new/corres/11/', New_Corres_11_View.as_view(), name='new_corres_11'),

    # ==== Не принятые заявлении
    path('not/accepted/', The_Choice_Not_Accepted_Admin.as_view(), name='The_Choice_Not_Accepted_Admin'),
    path('not/accepted/budget/9/', Not_Accepted_Budget_9_View.as_view(), name='not_accepted_budget_9'),
    path('not/accepted/budget/11/', Not_Accepted_Budget_11_View.as_view(), name='not_accepted_budget_11'),
    path('not/accepted/contract/9/', Not_Accepted_Contract_9_View.as_view(), name='not_accepted_contract_9'),
    path('not/accepted/contract/11/', Not_Accepted_Contract_11_View.as_view(), name='not_accepted_contract_11'),
    path('not/accepted/corres/11/', Not_Accepted_Corres_11_View.as_view(), name='not_accepted_contract_11'),

    # Ссылка для добавление
    path('budget/9/add/', add_statement_budget_9, name='statement_budget_9'),
    path('contract/9/add/', add_statement_contract_9, name='statement_contract_9'),
    path('budget/11/add/', add_statement_budget_11, name='statement_budget_11'),
    path('contract/11/add/', add_statement_contract_11, name='statement_contract_11'),
    path('corres/11/add/', add_statement_corres_11, name='statement_corres_11'),

]
