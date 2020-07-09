# Generated by Django 3.0.8 on 2020-07-07 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial - 副本'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.AddField(
            model_name='article',
            name='intro',
            field=models.TextField(blank=True, max_length=200, verbose_name='摘要'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tags'),
        ),
    ]