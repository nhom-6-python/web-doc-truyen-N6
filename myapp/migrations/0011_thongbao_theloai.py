# Generated by Django 4.2.7 on 2024-10-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_chap_truyen_alter_trang_chap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='thongbao',
            name='theloai',
            field=models.CharField(default='thông báo mới!!', max_length=255),
        ),
    ]