# Generated by Django 2.2.12 on 2020-04-23 18:11

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 17:06
from __future__ import unicode_literals

import logging

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

logger = logging.getLogger(__name__)


def forwards_func(apps, schema_editor):
    ProgramType = apps.get_model('course_metadata', 'ProgramType')
    ProgramTypeTranslation = apps.get_model('course_metadata', 'ProgramTypeTranslation')

    for program_type in ProgramType.objects.all():
        ProgramTypeTranslation.objects.update_or_create(
            master_id=program_type.pk,
            language_code=settings.PARLER_DEFAULT_LANGUAGE_CODE,
            name_t=program_type.name,
        )


def backwards_func(apps, schema_editor):
    ProgramType = apps.get_model('course_metadata', 'ProgramType')
    ProgramTypeTranslation = apps.get_model('course_metadata', 'ProgramTypeTranslation')

    for program_type in ProgramType.objects.all():
        try:
            translation = ProgramTypeTranslation.objects.get(master_id=program_type.pk, language_code=settings.LANGUAGE_CODE)
            program_type.name = translation.name_t
            program_type.save()  # Note this only calls Model.save()
        except ObjectDoesNotExist:
            # nothing to migrate
            logger.warning('Migrating data from ProgramTypeTranslation for master_id={} DoesNotExist'.format(program_type.pk))


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0243_auto_20200427_1514'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]
