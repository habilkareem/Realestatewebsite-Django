# Generated by Django 4.2.6 on 2024-04-07 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0011_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.realtor')),
            ],
        ),
    ]
