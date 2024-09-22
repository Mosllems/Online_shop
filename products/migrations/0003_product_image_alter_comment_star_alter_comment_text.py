# Generated by Django 5.1.1 on 2024-09-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='covers/', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.CharField(choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Perfect')], max_length=10, verbose_name='What is your score?'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Comment Text'),
        ),
    ]
