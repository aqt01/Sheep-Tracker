# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-25 09:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60, verbose_name='Country')),
                ('state', models.CharField(max_length=60, verbose_name='State/Province')),
                ('area', models.CharField(max_length=60, verbose_name='Area')),
                ('street', models.CharField(max_length=60, verbose_name='Street')),
                ('home', models.CharField(max_length=60, verbose_name='# ')),
                ('perimeter', models.IntegerField(null=True, verbose_name='Perimeter')),
            ],
        ),
        migrations.CreateModel(
            name='assistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance_avg', models.FloatField(verbose_name='promedio de asistencia')),
            ],
        ),
        migrations.CreateModel(
            name='assistance_avg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance_avg', models.FloatField(verbose_name='avrg of assistance')),
                ('start_date', models.DateField(verbose_name='From')),
                ('end_date', models.DateField(verbose_name='To')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('e_mail', models.CharField(max_length=120, verbose_name='E-mail')),
                ('country', models.CharField(max_length=60, verbose_name='Country')),
                ('state', models.CharField(max_length=60, verbose_name='State/Province')),
                ('area', models.CharField(max_length=60, verbose_name='Area')),
                ('street', models.CharField(max_length=60, verbose_name='Street')),
                ('home', models.CharField(max_length=60, verbose_name='# ')),
                ('perimeter', models.IntegerField(null=True, verbose_name='Perimeter')),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sheeps.Address')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('isChurch', models.BooleanField(default=False, verbose_name='Is a church?')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_cell', to='sheeps.Organization')),
            ],
            bases=('sheeps.address',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sheeps.Address')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('e_mail', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(max_length=15)),
                ('tellphone', models.CharField(max_length=15)),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
            ],
            bases=('sheeps.address',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sheeps.Contact')),
                ('role', models.CharField(choices=[('1', 'Invitado'), ('2', 'Miembro'), ('3', 'Lider'), ('4', 'Lider'), ('5', 'Pastor/a'), ('6', 'Pastor/a general')], max_length=80, verbose_name='Role')),
                ('pic', models.FileField(upload_to='')),
                ('organization_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_person', to='sheeps.Organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('sheeps.contact',),
        ),
        migrations.AddField(
            model_name='assistance',
            name='cell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheeps.Cell'),
        ),
        migrations.AddField(
            model_name='cell',
            name='consolidators',
            field=models.ManyToManyField(related_name='consolidators', to='sheeps.Person'),
        ),
        migrations.AddField(
            model_name='cell',
            name='guests',
            field=models.ManyToManyField(max_length=120, related_name='guests', to='sheeps.Person'),
        ),
        migrations.AddField(
            model_name='cell',
            name='supervisor',
            field=models.ManyToManyField(related_name='supervisors', to='sheeps.Person'),
        ),
        migrations.AddField(
            model_name='assistance',
            name='guests',
            field=models.ManyToManyField(to='sheeps.Person'),
        ),
    ]