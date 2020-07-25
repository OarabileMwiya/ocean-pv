# Generated by Django 3.1a1 on 2020-07-20 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    replaces = [('users', '0001_initial'), ('users', '0002_userprofile_receive_emails')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bio', models.TextField(null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=140, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('special_access', 'Can access the special page'),),
            },
        ),
        migrations.CreateModel(
            name='ProfileRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_name', models.CharField(max_length=100)),
                ('user_profile_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to='users.userprofile')),
                ('user_profile_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile2', to='users.userprofile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='profilerelation',
            constraint=models.UniqueConstraint(fields=('user_profile_1', 'user_profile_2'), name='profile_relations'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='receive_emails',
            field=models.BooleanField(default=True),
        ),
    ]