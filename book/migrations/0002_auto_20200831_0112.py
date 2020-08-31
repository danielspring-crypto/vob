# Generated by Django 2.1.5 on 2020-08-31 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(db_index=True, max_length=200)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('pdf', models.FileField(blank=True, upload_to='pdfs/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='book',
            index_together={('id', 'slug')},
        ),
    ]
