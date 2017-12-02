# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FB_Comment',
            fields=[
                ('comment_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('post_id', models.CharField(max_length=20)),
                ('page_id', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('sender_name', models.CharField(max_length=20)),
                ('sender_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(choices=[(1, 'Facebook'), (2, 'Twitter')])),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Closed'), (3, 'Archived')])),
                ('priority', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.FB_Comment')),
            ],
        ),
        migrations.CreateModel(
            name='TW_Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TW_Tweet'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.FB_Comment'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Issue'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='retweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TW_Tweet'),
        ),
    ]
