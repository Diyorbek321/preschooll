# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

import app.models as models
from app.models import Department

admin.site.register(Department)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_id', 'subject_class', 'subject_name')
    list_filter = ('id', 'subject_id', 'subject_class', 'subject_name')


class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'teacher_id',
        'name',
        'gender',
        'date_of_birth',
        'mobile',
        'joining_date',
        'qualification',
        'experience',
        'username',
        'email',
        'password',
        'address',
        'city',
        'state',
        'zip_code',
        'country',
    )
    list_filter = (
        'date_of_birth',
        'joining_date',
        'id',
        'teacher_id',
        'name',
        'gender',
        'mobile',
        'qualification',
        'experience',
        'username',
        'email',
        'password',
        'address',
        'city',
        'state',
        'zip_code',
        'country',
    )
    search_fields = ('name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'student_id',
        'gender',
        'date_of_birth',
        'student_class',
        'religion',
        'joining_date',
        'mobile_number',
        'admission_number',
        'section',
        'image',
        'father_name',
        'father_occupation',
        'father_mobile',
        'father_email',
        'mother_name',
        'mother_occupation',
        'mother_mobile',
        'mother_email',
    )
    list_filter = (
        'id',
        'first_name',
        'last_name',
        'student_id',
        'gender',
        'date_of_birth',
        'student_class',
        'religion',
        'joining_date',
        'mobile_number',
        'admission_number',
        'section',
        'image',
        'father_name',
        'father_occupation',
        'father_mobile',
        'father_email',
        'mother_name',
        'mother_occupation',
        'mother_mobile',
        'mother_email',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Teacher, TeacherAdmin)
_register(models.Subject, SubjectAdmin)
_register(models.Student, StudentAdmin)
