# Generated by Django 4.1 on 2022-11-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PendapatForum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=100)),
                ('angkatan', models.CharField(max_length=100)),
                ('pendapat', models.TextField()),
            ],
        ),
    ]