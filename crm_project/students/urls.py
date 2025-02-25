from django.urls import path

from.import views



urlpatterns = [

    path('dashboard', views.DashboardView.as_view(),name='dashboard'),

    path('students/', views.StudentsListView.as_view(),name = 'students'),

    path('forms/', views.FormsView.as_view(),name = 'forms'),

    path('student-detail/<str:uuid>/', views.StudentDetailView.as_view(),name = 'student-detail'),

    path('student-delete/<str:uuid>/',views.StudentDeleteView.as_view(),name = 'student-delete'),

    path('student-update/<str:uuid>/',views.StudentUpdateView.as_view(),name = 'student-update')





]