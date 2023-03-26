# Generated by Django 4.1.3 on 2022-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_photo_book_image_genre_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(
                blank=True, default='photo-placeholder.jpeg', upload_to='authors/'
            ),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(
                blank=True, default='product-placeholder.jpeg', upload_to='books/'
            ),
        ),
        migrations.AlterField(
            model_name='genre',
            name='image',
            field=models.ImageField(
                blank=True, default='image-placeholder.jpeg', upload_to='genres/'
            ),
        ),
    ]
