# Generated by Django 3.1.5 on 2021-01-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dnumber', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=150)),
                ('mgr_start_date', models.DateField()),
            ],
        ),
    ]