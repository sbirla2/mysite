from django.urls import path

from . import views
from . import forms

app_name = 'polls'
urlpatterns = [
    path('', views.HomePageView.as_view(), name=''),
    path('homepage', views.HomePageView.as_view(), name='homepage'),
    path('schedule', views.schedule, name='schedule'),
    path('schedule/list', views.find, name='schedule_list'),
    path('departments', views.DepartmentsListView.as_view(), name='departments'), 
    path('departments/create', views.DepartmentsCreateView.as_view(), name='departments_create'),
    path('departments/details/<slug:department_slug>', views.DepartmentsDetailView.as_view(), name='departments_detail'),
    path('departments/delete/<slug:department_slug>', views.DepartmentsDeleteView.as_view(), name='departments_delete'),
    path('departments/update/<slug:department_slug>', views.DepartmentsUpdateView.as_view(), name='departments_update'),
    path('classes', views.ClassesListView.as_view(), name='classes'),
    path('classes/details/<slug:class_slug>', views.ClassesDetailView.as_view(), name='classes_detail'),
    path('classes/create', views.ClassesCreateView.as_view(), name='classes_create'),
    path('classes/delete/<slug:class_slug>', views.ClassesDeleteView.as_view(), name='classes_delete'),
    path('classes/update/<slug:class_slug>', views.ClassesUpdateView.as_view(), name='classes_update'),
    path('sections', views.SectionsListView.as_view(), name='sections'),
    path('sections/details/<slug:section_slug>', views.SectionsDetailView.as_view(), name='sections_detail'),
    path('sections/create', views.SectionsCreateView.as_view(), name='sections_create'),
    path('sections/delete/<slug:section_slug>', views.SectionsDeleteView.as_view(), name='sections_delete'),
    path('sections/update/<slug:section_slug>', views.SectionsUpdateView.as_view(), name='sections_update'),
    path('professor', views.ProfessorListView.as_view(), name='professor'),
    path('professor/details/<slug:professor_slug>', views.ProfessorDetailView.as_view(), name='professor_detail'),
    path('professor/create', views.ProfessorCreateView.as_view(), name='professor_create'),
    path('professor/delete/<slug:professor_slug>', views.ProfessorDeleteView.as_view(), name='professor_delete'),
    path('professor/update/<slug:professor_slug>', views.ProfessorUpdateView.as_view(), name='professor_update'),

    # path('rel', views.rel, name='rel'),
    # path('rel/insert', views.insert, name='insert'),
    # path('rel/find', views.find, name='find'),
    # path('rel/delete', views.delete, name='delete'),
    # path('rel/update', views.update, name='update'),
    # path('rel/building', views.building, name='building'),   
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]