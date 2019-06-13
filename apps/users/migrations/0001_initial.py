# Generated by Django 2.2.2 on 2019-06-11 17:10

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssitStudy',
            fields=[
                ('number', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='学号')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('rangeCode', models.CharField(default='', max_length=30, verbose_name='随机码')),
                ('major', models.CharField(max_length=30, verbose_name='班级')),
                ('grade', models.CharField(max_length=30, verbose_name='年级')),
                ('job', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
            ],
            options={
                'verbose_name': '导向式助学',
                'verbose_name_plural': '导向式助学',
            },
        ),
        migrations.CreateModel(
            name='MyMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('st_id', models.CharField(max_length=50, unique=True, verbose_name='学号')),
                ('college', models.CharField(default='', max_length=20, verbose_name='学院')),
                ('major', models.CharField(default='', max_length=20, verbose_name='专业')),
                ('grade', models.CharField(default='', max_length=20, verbose_name='年级')),
                ('myclass', models.CharField(default='', max_length=10, verbose_name='班级')),
                ('phone_num', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('gender', models.CharField(choices=[('male', '男'), ('famale', '女')], default='男', max_length=6)),
                ('image', models.ImageField(default='my_info/default.png', upload_to='my_info/%Y/%m', verbose_name='头像')),
                ('favor', models.TextField(blank=True, max_length=50, null=True, verbose_name='专业兴趣')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '个人中心',
                'verbose_name_plural': '个人中心',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('colleage', models.CharField(default='计算机学院', max_length=40, verbose_name='学院')),
                ('is_admin', models.CharField(choices=[('stu', '学生'), ('admin', '管理员')], max_length=6, verbose_name='身份')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '添加用户',
                'verbose_name_plural': '添加用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
