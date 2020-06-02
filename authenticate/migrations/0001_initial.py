# Generated by Django 3.0.4 on 2020-03-28 11:37

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
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty')], default='Student', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authenticate.User')),
                ('enrollment_no', models.CharField(max_length=15)),
                ('semester', models.IntegerField(max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.Department')),
            ],
            bases=('authenticate.user',),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authenticate.User')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.Department')),
            ],
            bases=('authenticate.user',),
        ),
    ]