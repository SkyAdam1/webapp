# Generated by Django 3.1.4 on 2020-12-18 17:01

import apps.applications.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('project_name', models.CharField(db_index=True, max_length=150, verbose_name='Название проекта')),
                ('project_site', models.URLField(verbose_name='Ссылка на официальный сайт проекта')),
                ('data_project_start', models.DateField(verbose_name='Дата начала работы на проектом')),
                ('legal_entity', models.BooleanField(default=False, verbose_name='Юридическое лицо')),
                ('project_stage', models.CharField(max_length=150, verbose_name='На какой стадии развития находится ваш проект?')),
                ('project_description', models.TextField(verbose_name='Описание продукта/сервиса')),
                ('businessmodel_description', models.TextField(verbose_name='Описание бизнес-модели')),
                ('problem_decision', models.TextField(verbose_name='Какую проблему решает ваш продукт/сервис?')),
                ('consumer_decision', models.TextField(verbose_name='Как на данный момент потребители решают данную проблему?')),
                ('product_difference', models.TextField(verbose_name='Чем Ваш продукт / сервис отличается от текущего способа решения проблемы?')),
                ('have_photo', models.BooleanField(default=False, verbose_name='Есть ли фото/видео проекта?')),
                ('photo_video_project', models.URLField(blank=True, verbose_name='Ссылка на фото/видео продукта')),
                ('patentability', models.CharField(max_length=150, verbose_name='Насколько проработана патентоспособность продукта/услуги?')),
                ('market_size', models.CharField(max_length=150, verbose_name='Оцените объем Вашего рынка?')),
                ('marketing_description', models.TextField(verbose_name='Описание маркетинговой стратегии')),
                ('sale_strategy', models.TextField(verbose_name='Описание стратегии продаж')),
                ('desciption_risk', models.TextField(verbose_name='Описание существующих рисков')),
                ('client_count', models.IntegerField(verbose_name='Количество клиентов на данный момент')),
                ('previous_investors', models.CharField(max_length=500, verbose_name='Предыдущие инвесторы (ФИО, сумма инвестиций)')),
                ('middle_cost', models.CharField(max_length=50, verbose_name='Какая среднегодовая сумма издержек у вашей компании / проекта за последние 2 года')),
                ('budget_development', models.CharField(max_length=50, verbose_name='Какая сумма инвестирования вам необходима для дальнейшего развития?')),
                ('middle_revenue', models.CharField(max_length=50, verbose_name='Какая среднегодовая сумма выручки у вашей компании / проекта за последние 2 года?')),
                ('team_count', models.IntegerField(verbose_name='Количество человек в команде')),
                ('fio_team', models.TextField(verbose_name='ФИО членов команды')),
                ('team_education', models.CharField(max_length=500, verbose_name='Полученное образование членов команды')),
                ('team_experience', models.CharField(max_length=500, verbose_name='Опыт работы членов команды')),
                ('position_member', models.TextField(verbose_name='Текущая занимаемая должность членов команды')),
                ('residence_member', models.CharField(max_length=500, verbose_name='Текущее место жительства членов команды')),
                ('team_create', models.CharField(max_length=2000, verbose_name='Как вы познакомились и пришли к решению работать вместе?')),
                ('ready_relocate', models.BooleanField(verbose_name='Готова ли ваша команда переехать на время акселерационной программы в г.Грозный Чеченская Республика?')),
                ('ready_development', models.BooleanField(verbose_name='Готова ли ваша команда посвятить все свое время развитию проекта в соответствии с акселерационной программой?')),
                ('adress_company', models.CharField(max_length=150, verbose_name='Адрес компании')),
                ('inn_company', models.CharField(max_length=12, verbose_name='ИНН компании')),
                ('fio', models.CharField(db_index=True, max_length=150, verbose_name='ФИО контактного лица')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта контактного лица')),
                ('status', models.BooleanField(default=False, verbose_name='Статус заявки')),
                ('approved', models.BooleanField(default=False, verbose_name='Одобрено/Не добрено')),
                ('upload', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст замечания')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, verbose_name='Просмотрено')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(null=True, upload_to='reporting/', validators=[apps.applications.validators.validate_file_extension])),
                ('year', models.IntegerField(default=2020)),
                ('quarter', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='За какой квартал отчет?')),
                ('status', models.BooleanField(default=False, verbose_name='отправлен или нет')),
                ('approved', models.BooleanField(default=False, verbose_name='одобрен или нет')),
            ],
            options={
                'ordering': ['-year', '-quarter'],
            },
        ),
        migrations.CreateModel(
            name='DesignatedExpert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='Оценка')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.application')),
            ],
        ),
    ]