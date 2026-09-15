from django.contrib import admin

from .models import Student, Course, Enrollment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student_name",
        "email",
        "age",
        "created_at",
    )

    search_fields = (
        "student_name",
        "email",
    )

    ordering = ("id",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course_name",
        "course_code",
        "duration_months",
    )

    search_fields = (
        "course_name",
        "course_code",
    )

    ordering = ("id",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "student",
        "course",
        "enrollment_date",
    )

    list_filter = (
        "course",
        "enrollment_date",
    )

    search_fields = (
        "student__student_name",
        "course__course_name",
    )

    ordering = ("id",)
    