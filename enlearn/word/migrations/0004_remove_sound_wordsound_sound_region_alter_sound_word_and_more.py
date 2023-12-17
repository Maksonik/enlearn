# Generated by Django 4.2.7 on 2023-11-28 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_description_word_form_word_sound_word_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sound',
            name='wordsound',
        ),
        migrations.AddField(
            model_name='sound',
            name='region',
            field=models.CharField(choices=[('UK', 'United Kingdom'), ('US', 'United States')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sound',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sounds', to='word.word'),
        ),
        migrations.DeleteModel(
            name='WordSound',
        ),
    ]