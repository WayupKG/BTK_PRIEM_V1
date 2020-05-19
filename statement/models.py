import os
import uuid

from django.db.models import *
from django.contrib.auth.models import User


class Public_9_budget_Manager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(certificate_status='Свидетельство',
                                             budget_contract='Бюджет').order_by('-created')


class Public_9_Contract_Manager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(certificate_status='Свидетельство',
                                             budget_contract='Контракт').order_by('-created')


class Public_11_Contract_Manager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(certificate_status='Аттестат') | Q(certificate_status='Диплом'),
                                             Q(budget_contract='Контракт'),
                                             Q(form_training='Очный')).order_by('-created')


class Public_11_Corres_Manager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(certificate_status='Аттестат') | Q(certificate_status='Диплом'),
                                             Q(budget_contract='Контракт'),
                                             Q(form_training='Заочный')).order_by('-created')


class Statement(Model):
    """Заявления"""

    FLOOR_STATUS = (
        ('Мужчина', 'Мужчина'),
        ('Женшина', 'Женшина')
    )

    STATUS = (
        ('В ожидании', 'В ожидании'),
        ('Принят', 'Принят'),
        ('Не принят', 'Не принят')
    )
    reg_number = IntegerField(default=0)
    registor_index = CharField(max_length=20, blank=True, null=True)
    first_name = CharField('Имя:', max_length=50)
    last_name = CharField('Фамилия:', max_length=50)
    patronymic = CharField('Отчество:', max_length=50, blank=True, null=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name='statement')
    slug = SlugField(max_length=100, unique=True)
    graduated = CharField('Наименование учебного заведения:', max_length=150)
    near = CharField('Город, Район', max_length=70)
    certificate_status = CharField('и получил(а): ', max_length=25, default='Свидетельство')
    certificate_number = CharField('Серия и номер (свидетельство, аттестат или диплом)', max_length=50)
    certificate_date = IntegerField(verbose_name='Год выдачи (свидетельство, аттестат или диплом)')
    date_of_birth = DateField(verbose_name='Дата рождения')
    nationality = CharField('Национальность', max_length=50)
    passport_or_certificate = CharField('Номер паспорта или свидетельство', max_length=70)
    floor = CharField(verbose_name='Пол', max_length=10, choices=FLOOR_STATUS, default='Мужчина')
    form_training = CharField('Форма обучение', max_length=5, default='Очный')
    budget_contract = CharField('Бюджет контракт', max_length=10, default='Контракт')
    specialty = CharField('Специальност', max_length=100)
    father = CharField('Отец', max_length=100)
    father_phone = CharField('Номер телефона', max_length=50)
    mother = CharField('Мать', max_length=100)
    mother_phone = CharField('Номер телефона', max_length=50)
    place_of_residence = CharField('Место жителство студента', max_length=150)
    phone_student = CharField('Номер телефона студента', max_length=50)
    image_student = ImageField(verbose_name='Фото студента', upload_to='Student_Photo/')
    image_passport_or_certificate = ImageField(verbose_name='Фото паспорта или свидетельсто о рд.',
                                               upload_to='Statements/')
    image_certificate = ImageField(verbose_name='Фото (свидетельство, аттестат или диплом).',
                                   upload_to='certificate/', blank=True, null=True)
    status = CharField('Статус', max_length=10, choices=STATUS, default='В ожидании')
    updated = DateTimeField(auto_now=True)  # -- Дата обновлении
    created = DateTimeField(auto_now_add=True)  # -- Дата создание заявление

    responsible = CharField('Ответственный', max_length=100, default='В ожидании')
    created_the_accepted = DateTimeField(auto_now_add=True)  # -- Дата Приняти заявление

    image_certificate_priom = CharField(verbose_name='Сертификат',
                                        max_length=200, blank=True, null=True)

    # Менеджер
    objects = Manager()
    budget_9 = Public_9_budget_Manager()
    contact_9 = Public_9_Contract_Manager()
    contact_11 = Public_11_Contract_Manager()
    corres_11 = Public_11_Corres_Manager()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        ordering = ('-reg_number',)
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявление'


class Review(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='review')
    text = CharField(max_length=250)
    statement = ForeignKey(Statement, on_delete=CASCADE, related_name='review_statement')
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.statement}'

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
