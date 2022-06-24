# Generated by Django 4.0.4 on 2022-06-23 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_app', '0002_cart_alter_category_options_cartitem_cart_products'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receipt_items', to='shop_app.product')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_items', to='payments_app.receipt')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='products',
            field=models.ManyToManyField(related_name='receipts', through='payments_app.ReceiptItem', to='shop_app.product'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to=settings.AUTH_USER_MODEL),
        ),
    ]