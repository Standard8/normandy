# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 22:25
# flake8: noqa
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0026_recipe_approver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('active', models.BooleanField(default=True)),
                ('approval', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approval_request', to='recipes.Approval')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ApprovalRequestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.TextField()),
                ('approval_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipes.ApprovalRequest')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='approver',
        ),
        migrations.AddField(
            model_name='approvalrequest',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approval_requests', to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='approval',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipes.Approval'),
        ),
    ]