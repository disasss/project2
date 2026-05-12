from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/', views.student_list, name='student_list_alias'),
    path('hello/', views.hello, name='hello'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register'), name='logout'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]

