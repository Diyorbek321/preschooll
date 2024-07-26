from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    Gender = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    teacher_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=20)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)


class Subject(models.Model):
    subject_id = models.CharField(max_length=100)
    subject_class = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)


role_choices = (
    ('student', 'student'),
    ('teacher', 'teacher'),
    ('admin', 'admin')
)


class Department(models.Model):
    department_id = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    department_hod = models.CharField(max_length=255)
    department_start = models.IntegerField()
    department_student = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=100)
    section = models.CharField(max_length=10)
    image = models.ImageField(upload_to='students/', blank=True)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField()
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField()
    location = models.CharField(max_length=255, blank=True)
    permanent_address = models.TextField(blank=True)


class Fees(models.Model):
    student_id = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    fees_type = models.CharField(max_length=255)
    amount = models.IntegerField()
    paid_date = models.DateTimeField()


class Expenses(models.Model):
    expense_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    source = models.CharField(max_length=255)
    purchase_date = models.DateTimeField()
    purchase_by = models.CharField(max_length=255)


class Holiday(models.Model):
    holiday_id = models.CharField(max_length=255)
    holiday_name = models.CharField(max_length=255)
    type_holiday = models.CharField(max_length=255)
    start_date = models.TimeField()
    end_date = models.TimeField()


class Library(models.Model):
    Book_type_choice = [
        ('Book', 'Book'),
        ('DVD', 'DVD'),
        ('CD', 'CD'),
        ('Newspaper', 'Newspaper'),
    ]
    Book_status = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
    ]
    Book_language = [
        ('English', 'English'),
        ('Turkish', 'Turkish'),
        ('Chinese', 'Chinese'),
        ('Spanish', 'Spanish'),
        ('Arabic', 'Arabic'),
    ]
    book_id = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    book_language = models.CharField(max_length=255, choices=Book_language)
    department = models.CharField(max_length=255)
    book_class = models.CharField(max_length=255)
    book_type = models.CharField(max_length=150, choices=Book_type_choice)
    book_status = models.CharField(max_length=150, choices=Book_status)


class Salary(models.Model):
    Gender = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    staff_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=Gender)
    joining_date = models.DateField()
    amount = models.IntegerField()


class Exam(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_class = models.CharField(max_length=255)
    exam_subject = models.CharField(max_length=255)
    exam_fees = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_date = models.DateField()


class Event(models.Model):
    event_id = models.CharField(max_length=255)
    event_name = models.CharField(max_length=155)
    event_date = models.DateField()


class TimeTable(models.Model):
    teacher_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    subject_class = models.CharField(max_length=155)
    section = models.CharField(max_length=155)
    subject = models.CharField(max_length=155)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    rating = models.BooleanField(default=False)

