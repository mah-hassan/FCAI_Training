# Generated by Django 4.1.7 on 2023-03-27 15:47

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
            name='Nominee_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('phone_no', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=200, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('community', models.CharField(choices=[('1', 'اللجنة العلمية'), ('2', 'اللجنة الرياضية'), ('3', 'اللجنة الاجتماعية'), ('4', 'أسرة الجوالة و الخدمات'), ('5', 'اللجنة الثقافية'), ('6', 'اللجنة الفنية'), ('7', 'لجنة الاسر و الرحلات')], max_length=20)),
                ('collegeYear', models.IntegerField(max_length=20, null=True)),
                ('rec_letter', models.FileField(upload_to='')),
                ('final_list', models.BooleanField(default=False)),
                ('Numofvotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('Student_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.IntegerField()),
                ('nominee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.nominee_user')),
                ('voter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='nominee_user',
            name='nominee_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='training.usermodel'),
        ),
        migrations.CreateModel(
            name='Contention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contention_id', models.IntegerField()),
                ('reason', models.TextField()),
                ('nominee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.nominee_user')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
