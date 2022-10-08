# Generated by Django 2.1 on 2018-08-20 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
        ('subscribers', '0005_auto_20180816_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='lists.MailingList')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'db_table': 'colossus_tags',
            },
        ),
        migrations.AddField(
            model_name='subscriber',
            name='tags',
            field=models.ManyToManyField(related_name='subscribers', to='subscribers.Tag', verbose_name='tags'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('name', 'mailing_list')},
        ),
    ]
