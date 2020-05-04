# Generated by Django 3.0.5 on 2020-05-04 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'class_dept',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('subject_number', models.CharField(db_column='Subject_Number', max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=100, null=True)),
            ],
            options={
                'db_table': 'classes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('netid', models.CharField(db_column='NetID', max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=30, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=30, null=True)),
            ],
            options={
                'db_table': 'professor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('crn', models.CharField(db_column='CRN', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('credithours', models.CharField(blank=True, db_column='CreditHours', max_length=30, null=True)),
                ('section', models.CharField(blank=True, db_column='Section', max_length=5, null=True)),
                ('sectiontype', models.CharField(blank=True, db_column='SectionType', max_length=5, null=True)),
                ('starttime', models.CharField(blank=True, db_column='StartTime', max_length=15, null=True)),
                ('endtime', models.CharField(blank=True, db_column='EndTime', max_length=15, null=True)),
                ('dayofweek', models.CharField(blank=True, db_column='DayOfWeek', max_length=10, null=True)),
                ('gpa', models.CharField(blank=True, db_column='GPA', max_length=5, null=True)),
                ('subject_number', models.ForeignKey(blank=True, db_column='Subject_Number', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Classes')),
            ],
            options={
                'db_table': 'sections',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.ForeignKey(blank=True, db_column='CRN', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Sections')),
                ('netid', models.ForeignKey(blank=True, db_column='NetID', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Professor')),
            ],
            options={
                'db_table': 'teaches',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='professor',
            name='sections_teaches',
            field=models.ManyToManyField(through='polls.Teaches', to='polls.Sections'),
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_id', models.CharField(db_column='Dept_ID', max_length=3, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, db_column='Dept_Name', max_length=40, null=True)),
                ('classes_contains', models.ManyToManyField(through='polls.ClassDept', to='polls.Classes')),
            ],
            options={
                'db_table': 'departments',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='classdept',
            name='dept',
            field=models.ForeignKey(blank=True, db_column='Dept_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Departments'),
        ),
        migrations.AddField(
            model_name='classdept',
            name='subject_number',
            field=models.ForeignKey(blank=True, db_column='Subject_Number', null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Classes'),
        ),
    ]
