# Generated by Django 4.2.1 on 2023-06-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('getfor', models.CharField(choices=[('school', 'School'), ('coaching', 'Coaching'), ('personal', 'Personal'), ('institution', 'Institution'), ('college', 'College'), ('other', 'Other')], max_length=100)),
                ('Class', models.CharField(choices=[('class_6', 'Class 6'), ('class_7', 'Class 7'), ('class_8', 'Class 8'), ('class_9', 'Class 9'), ('class_10', 'Class 10'), ('class_11', 'Class 11'), ('class_12', 'Class 12')], max_length=100)),
                ('product', models.CharField(choices=[('animation_video', 'Animation Video'), ('notes_with_mind_map', 'Notes with mind map'), ('animation_video', 'Animation Video')], max_length=200)),
            ],
        ),
    ]
