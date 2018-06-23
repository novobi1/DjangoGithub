from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),

]
