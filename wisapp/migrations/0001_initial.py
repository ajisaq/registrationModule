# Generated by Django 2.2.6 on 2019-10-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('dept_id', models.CharField(max_length=12)),
                ('hod', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bvn', models.CharField(max_length=11)),
                ('lga', models.CharField(max_length=20)),
                ('nimc', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=25)),
                ('disability', models.CharField(max_length=150)),
                ('other_name', models.CharField(max_length=25)),
                ('next_of_kin', models.CharField(max_length=25)),
                ('nationality', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=30)),
                ('salary_amount', models.IntegerField(default=0)),
                ('place_of_work', models.CharField(max_length=25)),
                ('account_number', models.CharField(max_length=10)),
                ('state_of_origin', models.CharField(max_length=20)),
                ('passport', models.ImageField(upload_to='passports/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wisapp.Department')),
            ],
        ),
    ]