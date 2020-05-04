import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200, default="0000")
#     def __str__(self):
#         return self.username


class Classes(models.Model):
    subject_number = models.CharField(db_column='Subject_Number', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    class_slug = models.SlugField(unique=False, null=True)
    def get_absolute_url(self):
        return reverse('polls:classes_detail', kwargs={'subject': self.class_slug})
    def save(self, *args, **kwargs):
        value = self.subject_number
        self.class_slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.subject_number
    class Meta:
        managed = True
        db_table = 'classes'


class Departments(models.Model):
    dept_id = models.CharField(db_column='Dept_ID', primary_key=True, max_length=3)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    classes_contains = models.ManyToManyField(Classes, through='ClassDept')
    def get_absolute_url(self):
        return reverse('polls:departments_detail', kwargs={'department_slug': self.dept_id})
    def __str__(self):
        return self.dept_id + ' ' + self.dept_name
    class Meta:
        managed = True
        db_table = 'departments'


class ClassDept(models.Model):
    dept = models.ForeignKey('Departments', on_delete=models.CASCADE, db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    subject_number = models.ForeignKey('Classes', on_delete=models.CASCADE, db_column='Subject_Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'class_dept'


class Sections(models.Model):
    crn = models.CharField(db_column='CRN', primary_key=True, max_length=5)  # Field name made lowercase.
    subject_number = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='Subject_Number', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    credithours = models.CharField(db_column='CreditHours', max_length=30, blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sectiontype = models.CharField(db_column='SectionType', max_length=5, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=15, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='EndTime', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dayofweek = models.CharField(db_column='DayOfWeek', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gpa = models.CharField(db_column='GPA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.crn + ' ' + self.name
    def get_absolute_url(self):
        return reverse('polls:sections_detail', kwargs={'section_slug': self.crn})
    class Meta:
        managed = True
        db_table = 'sections'


class Professor(models.Model):
    netid = models.CharField(db_column='NetID', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True, null=True)  # Field name made lowercase.
    sections_teaches = models.ManyToManyField(Sections, through='Teaches')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('polls:professor_detail', kwargs={'professor_slug': self.netid})
    class Meta:
        managed = True
        db_table = 'professor'


class Teaches(models.Model):
    netid = models.ForeignKey(Professor, on_delete=models.CASCADE, db_column='NetID', blank=True, null=True)  # Field name made lowercase.
    crn = models.ForeignKey(Sections, on_delete=models.CASCADE, db_column='CRN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'teaches'

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text