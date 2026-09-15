from django.shortcuts import render
from .models import Student, Course, Enrollment


def dashboard(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    enrollments = Enrollment.objects.select_related(
        "student",
        "course"
    )

    context = {
        "students": students,
        "courses": courses,
        "enrollments": enrollments,
    }

    return render(request, "students/dashboard.html", context)