# Generated by Django 4.1.2 on 2022-11-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
