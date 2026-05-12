from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, StudentForm
from .models import Student


@login_required
def profile(request):
    user = request.user
    return render(request, 'students/profile.html', {'user': user})

def hello(request):
    return HttpResponse("Добро пожаловать на сайт колледжа!")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'students/register.html', {'form': form})


@login_required
def student_list(request):
    can_manage_students = request.user.is_staff
    edit_student = None
    if request.method == 'POST':
        if not can_manage_students:
            raise PermissionDenied
        student_id = request.POST.get('student_id')
        if student_id:
            edit_student = get_object_or_404(Student, id=student_id)
            form = StudentForm(request.POST, request.FILES, instance=edit_student)
        else:
            form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        edit_id = request.GET.get('edit')
        if edit_id:
            if not can_manage_students:
                return redirect('student_list')
            edit_student = get_object_or_404(Student, id=edit_id)
        form = StudentForm(instance=edit_student) if can_manage_students else None

    students = Student.objects.all()
    return render(request, 'students/index.html', {
        'students': students,
        'form': form,
        'edit_student': edit_student,
        'can_manage_students': can_manage_students,
    })


@login_required
def edit_student(request, student_id):
    if not request.user.is_staff:
        raise PermissionDenied
    return redirect(f"/students/?edit={student_id}")


@login_required
def delete_student(request, student_id):
    if not request.user.is_staff:
        raise PermissionDenied
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
    return redirect('student_list')

