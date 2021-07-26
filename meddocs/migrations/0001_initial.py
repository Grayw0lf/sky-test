# Generated by Django 3.2.5 on 2021-07-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.IntegerField(verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания')),
                ('result', models.IntegerField(null=True, verbose_name='Исход лечения')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='meddocs.patient', verbose_name='Пациент')),
            ],
            options={
                'verbose_name': 'Случай лечения',
                'verbose_name_plural': 'Случаи лечения',
            },
        ),
        migrations.CreateModel(
            name='MedicalDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок документа')),
                ('date_doc', models.DateField(verbose_name='Дата документа')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicaldocs', to='meddocs.patient', verbose_name='Пациент')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicaldocs', to='meddocs.treatment', verbose_name='Случай лечения')),
            ],
            options={
                'verbose_name': 'Медицинский документ',
                'verbose_name_plural': 'Медицинские документы',
            },
        ),
        migrations.CreateModel(
            name='BodyDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.JSONField(verbose_name='Наполнение документа')),
                ('medicaldoc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bodydoc', to='meddocs.medicaldoc', verbose_name='Медицинский документ')),
            ],
            options={
                'verbose_name': 'Тело документа',
                'verbose_name_plural': 'Тело документа',
            },
        ),
    ]
