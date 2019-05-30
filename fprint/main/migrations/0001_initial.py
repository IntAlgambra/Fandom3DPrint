# Generated by Django 2.2.1 on 2019-05-14 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=200)),
                ('sender_email', models.EmailField(max_length=254)),
                ('question_text', models.TextField()),
                ('question_file', models.FileField(blank=True, upload_to='clients_files/')),
            ],
        ),
    ]
