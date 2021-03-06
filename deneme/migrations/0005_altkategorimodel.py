# Generated by Django 3.1.5 on 2021-03-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deneme', '0004_auto_20210301_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltKategoriModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('alt_kategoriler', models.ManyToManyField(related_name='alturun', to='deneme.KategoriModel')),
            ],
            options={
                'verbose_name': 'Alt_Kategori',
                'verbose_name_plural': 'Alt_Kategoriler',
                'db_table': 'alt_kategori',
            },
        ),
    ]
