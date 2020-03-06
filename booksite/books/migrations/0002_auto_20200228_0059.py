# Generated by Django 3.0.3 on 2020-02-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '类别', 'verbose_name_plural': '类别'},
        ),
        migrations.AlterField(
            model_name='books',
            name='published_date',
            field=models.DateField(verbose_name='出版时间'),
        ),
    ]
