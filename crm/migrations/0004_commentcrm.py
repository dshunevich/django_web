# Generated by Django 3.1.7 on 2021-03-25 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210325_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('comment_binging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
