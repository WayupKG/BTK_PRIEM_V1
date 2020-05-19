from django.contrib import admin
from .models import *


@admin.register(Statement)
class AdminStatement(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'created', 'updated')


@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ('statement', 'user', 'created')
