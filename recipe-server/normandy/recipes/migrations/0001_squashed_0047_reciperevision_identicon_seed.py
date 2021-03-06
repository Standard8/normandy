# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-16 17:30
# flake8: noqa
from __future__ import unicode_literals

import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import normandy.recipes.fields
import normandy.recipes.validators


class Migration(migrations.Migration):
    replaces = [('recipes', '0001_initial'), ('recipes', '0002_auto_20151231_1952'),
                ('recipes', '0003_auto_20160112_2222'), ('recipes', '0004_auto_20160112_2312'),
                ('recipes', '0005_auto_20160113_0113'), ('recipes', '0003_auto_20160113_0046'),
                ('recipes', '0006_merge'), ('recipes', '0007_auto_20160120_0003'),
                ('recipes', '0008_auto_20160122_0228'), ('recipes', '0009_recipe_locale'),
                ('recipes', '0010_auto_20160122_0715'), ('recipes', '0011_auto_20160202_2325'),
                ('recipes', '0012_action_arguments_schema'),
                ('recipes', '0013_auto_20160204_2155'), ('recipes', '0014_auto_20160204_2337'),
                ('recipes', '0015_auto_20160217_1819'), ('recipes', '0016_auto_20160219_0101'),
                ('recipes', '0017_auto_20160218_2024'), ('recipes', '0018_countries'),
                ('recipes', '0019_add_revision_id'), ('recipes', '0020_auto_20160316_1947'),
                ('recipes', '0021_migrate_to_single_actions'),
                ('recipes', '0022_auto_20160317_0008'), ('recipes', '0023_auto_20160324_2333'),
                ('recipes', '0024_recipe_filter_expression'),
                ('recipes', '0025_auto_20160429_2357'), ('recipes', '0026_recipe_approver'),
                ('recipes', '0027_auto_20160509_2225'), ('recipes', '0028_auto_20160524_1756'),
                ('recipes', '0029_recipe_last_updated'), ('recipes', '0030_auto_20160816_2154'),
                ('recipes', '0031_recipe_signing'), ('recipes', '0032_remove_auto_now'),
                ('recipes', '0033_migrate_surveys'), ('recipes', '0034_recipe_revisions'),
                ('recipes', '0035_revision_data'), ('recipes', '0036_remove_old_recipe_fields'),
                ('recipes', '0037_auto_20170113_0627'),
                ('recipes', '0038_remove_invalid_signatures'),
                ('recipes', '0039_approval_requests'), ('recipes', '0040_approvalrequest_comment'),
                ('recipes', '0041_remove_invalid_signatures'),
                ('recipes', '0042_remove_invalid_signatures'),
                ('recipes', '0043_auto_20170727_1634'), ('recipes', '0044_auto_20170801_0010'),
                ('recipes', '0045_update_action_hashes'), ('recipes', '0046_reset_signatures'),
                ('recipes', '0047_reciperevision_identicon_seed')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255, unique=True)),
                ('implementation', models.TextField()),
                ('implementation_hash', models.CharField(editable=False, max_length=71)),
                ('arguments_schema_json', models.TextField(default='{}', validators=[normandy.recipes.validators.validate_json])),
            ],
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ApprovalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.NullBooleanField()),
                ('comment', models.TextField(null=True)),
                ('approver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_requests', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approval_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('slug',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-enabled', '-latest_revision__updated'],
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RecipeRevision',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('arguments_json', models.TextField(default='{}', validators=[normandy.recipes.validators.validate_json])),
                ('extra_filter_expression', models.TextField()),
                ('identicon_seed', normandy.recipes.fields.IdenticonSeedField(max_length=64)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_revisions', to='recipes.Action')),
                ('channels', models.ManyToManyField(to='recipes.Channel')),
                ('countries', models.ManyToManyField(to='recipes.Country')),
                ('locales', models.ManyToManyField(to='recipes.Locale')),
                ('parent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='recipes.RecipeRevision')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='recipes.Recipe')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipe_revisions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('public_key', models.TextField()),
                ('x5u', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='approved_revision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_for_recipe', to='recipes.RecipeRevision'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='latest_revision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='latest_for_recipe', to='recipes.RecipeRevision'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='signature',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipes.Signature'),
        ),
        migrations.AddField(
            model_name='approvalrequest',
            name='revision',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='approval_request', to='recipes.RecipeRevision'),
        ),
        migrations.AddField(
            model_name='action',
            name='signature',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action', to='recipes.Signature'),
        ),
    ]
